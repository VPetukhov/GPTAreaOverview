import pickle
import os
import numpy as np

from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression

from label_studio_ml.model import LabelStudioMLBase


class SimpleTextClassifier(LabelStudioMLBase):

    def __init__(self, **kwargs):
        # don't forget to initialize base class...
        super(SimpleTextClassifier, self).__init__(**kwargs)

        # then collect all keys from config which will be used to extract data from task and to form prediction
        # Parsed label config contains only one output of <Choices> type
        assert len(self.parsed_label_config) == 1
        self.from_name, self.info = list(self.parsed_label_config.items())[0]
        assert self.info['type'] == 'Choices'

        # the model has only one textual input
        assert len(self.info['to_name']) == 1
        assert len(self.info['inputs']) == 1
        assert self.info['inputs'][0]['type'] == 'Text'
        self.to_name = self.info['to_name'][0]
        self.value = self.info['inputs'][0]['value']

        if not self.train_output:
            # If there is no trainings, define cold-started the simple TF-IDF text classifier
            self.reset_model()
            # This is an array of <Choice> labels
            self.labels = np.array(self.info['labels'])
            # # make some dummy initialization
            self.model.fit(
                [np.random.randn(1536) for _ in range(20)],
                [np.random.rand(len(self.labels)) > 0.5 for _ in range(20)]
            )
            print('Initialized with from_name={from_name}, to_name={to_name}, labels={labels}'.format(
                from_name=self.from_name, to_name=self.to_name, labels=str(self.labels)
            ))
        else:
            # otherwise load the model from the latest training results
            self.model_file = self.train_output['model_file']
            with open(self.model_file, mode='rb') as f:
                self.model = pickle.load(f)
            # and use the labels from training outputs
            self.labels = np.array(self.train_output['labels'])
            print('Loaded from train output with from_name={from_name}, to_name={to_name}, labels={labels}'.format(
                from_name=self.from_name, to_name=self.to_name, labels=str(self.labels)
            ))

    def reset_model(self):
        # self.model = LogisticRegression(C=10, verbose=True)
        self.model = MultiOutputClassifier(estimator=LogisticRegression(n_jobs=4, C=100), n_jobs=4)

    def predict(self, tasks, **kwargs):
        # collect input texts
        input_embeddings = []
        for task in tasks:
            input_embeddings.append(task['data']['embedding'])

        # get model predictions
        labels = [self.labels[m] for m in self.model.predict(input_embeddings)]
        scores = np.c_[[x.max(axis=1) for x in self.model.predict_proba(input_embeddings)]].min(axis=0)
        predictions = []
        for labs, score in zip(labels, scores):
            # prediction result for the single task
            result = [{
                'from_name': self.from_name,
                'to_name': self.to_name,
                'type': 'choices',
                'value': {'choices': list(labs)}
            }]

            # expand predictions with their scores for all tasks
            predictions.append({'result': result, 'score': score})

        return predictions

    def fit(self, completions, workdir=None, **kwargs):
        input_embeddings = []
        output_labels = []
        for completion in completions:
            # print(completion)
            # get input text from task data
            if completion['annotations'][0].get('skipped') or completion['annotations'][0].get('was_cancelled'):
                continue

            results = completion['annotations'][0]['result']
            if len(results) == 0:
                continue

            input_embeddings.append(completion['data']['embedding'])

            # get an annotation
            choices = results[0]['value']['choices']
            output_labels.append([a in choices for a in self.labels])

        # train the model
        if len(input_embeddings) > 0:
            self.reset_model()
            self.model.fit(input_embeddings, output_labels)
        else:
            print('WARNING: No training data found')

        # save output resources
        model_file = os.path.join(workdir, 'model.pkl')
        with open(model_file, mode='wb') as fout:
            pickle.dump(self.model, fout)

        train_output = {
            'labels': list(self.labels),
            'model_file': model_file
        }
        return train_output
