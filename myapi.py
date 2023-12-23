import getpass
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import JSONLoader

import json
from pathlib import Path
from pprint import pprint

# Load the .env file
load_dotenv()

# Get the API key from the environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")

# If the API key is not set, ask the user to provide it
if not google_api_key:
    google_api_key = getpass.getpass("Provide your Google API Key")

# Using JSONLoader to load the data
loader = JSONLoader(
    file_path='cleaned_uvu-data-1.json',
    jq_schema='.[].html',
    text_content=False)

data = loader.load()

pprint(data)

# llm = ChatGoogleGenerativeAI(model="gemini-pro")
# result = llm.invoke("Write a ballad about LangChain")
# print(result.content)