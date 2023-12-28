from langchain.document_loaders import JSONLoader
import json
from pprint import pprint

def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def load_data(file_path):
    data = load_json(file_path)

    loader = JSONLoader(
        file_path=file_path,
        jq_schema='.[]',
        text_content=False,
    )

    loaded_data = loader.load()

    # Split by each index in the list of loaded data
    for index, loaded in enumerate(loaded_data):
        print(f'Index: {index}')
        pprint(loaded)
        print('\n')

