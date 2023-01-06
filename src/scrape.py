from math import ceil

import requests
import time
from pandas import DataFrame

from tqdm.auto import trange

import openai
from time import sleep


def get_safe(url, n_tries=5, **kwargs):
    response = None
    for _ in range(n_tries):
        try:
            response = requests.get(url, **kwargs)
            if response.status_code == 200:
                return response
            else:
                print('Error: ', response.status_code, ' ; retrying...')
                time.sleep(2)
        except Exception as e:
            print("Error in request: ", e, ' ; retrying...')
            time.sleep(10)

    return response


def scrape_s2(query: str, n: int = 100, fields: str = '', year: str = '2014-'):
    if fields == '':
        fields = 'title,abstract,year,citationCount,influentialCitationCount'

    s2_url = 'https://api.semanticscholar.org/graph/v1/paper/search'
    limit = min(n, 100)
    req_res = []
    for i in trange(ceil(n / limit)):
        url = f'{s2_url}?query="{query}"&limit={limit}&offset={limit * i}&fields={fields}&year={year}'
        req = get_safe(url)
        if req.status_code != 200:
            print(f'Error {req.status_code}: {req.text}')
            continue

        req_res += req.json()['data']
    req_res = DataFrame(req_res).dropna()

    return req_res


def query_openai(query: str, req_type: str, max_try: int = 3, **kwargs):
    for _ in range(max_try):
        try:
            if req_type == 'search':
                response = openai.Embedding.create(input=query, **kwargs)
                return response['data'][0]['embedding'], response["usage"]["total_tokens"]

            if req_type == 'completion':
                response = openai.Completion.create(prompt=query, **kwargs)
                return response["choices"][0]["text"], response["usage"]["total_tokens"]

            if req_type == "edit":
                response = openai.Edit.create(input=query, **kwargs)
                return response["choices"][0]["text"], response["usage"]["total_tokens"]

            raise ValueError(f'Invalid request type: {req_type}')

        except Exception as e:
            print("Error in request: ", e)
            sleep(3)

    return None, None
