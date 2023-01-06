import requests
import pandas as pd
from pandas import DataFrame
import os


api_key = os.getenv("HASURA_API_KEY")


def save_field(pid: int, value: str, field: str):
    query = f"""
    mutation {{
    update_ml_scrnaseq_papers_by_pk(
        pk_columns: {{pubmed_id: {pid}}}
        _set: {{{field}: "{value}"}}
    ) {{pubmed_id}}
    }}
    """

    res = requests.post(
        "https://sealver.in/hasura/v1/graphql",
        json={'query': query},
        auth=requests.auth.HTTPBasicAuth('user', api_key)
    ).json()

    if res.get('data', {}).get('update_ml_scrnaseq_papers_by_pk', {}).get('pubmed_id', 0) != pid:
        print(res)
        print(f"Error for pid {pid}")
        print()


def get_data():
    paps = requests.get(
        "https://sealver.in/hasura/api/rest/scrnaseq_papers/get",
        auth = requests.auth.HTTPBasicAuth('user', api_key)
    )
    
    return DataFrame(paps.json()['ml_scrnaseq_papers']).set_index('pubmed_id')
