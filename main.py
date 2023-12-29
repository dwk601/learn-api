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

    return loaded_data

data = load_data('data.json')

def chunk_data(data, chunk_size):
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        chunks.append(chunk)
    return chunks

chunk_size = 3
chunks = chunk_data(data, chunk_size)

# for i, chunk in enumerate(chunks):
#     print(f'Chunk {i}: {chunk}')