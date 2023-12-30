from langchain.document_loaders import JSONLoader
import json
from pprint import pprint

import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

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

text = data[0]
pprint(text)

# model = 'models/embedding-001'
# embedding = genai.embed_content(model=model,
#                                 content=text,
#                                 task_type="retrieval_document")

# print(embedding)