import getpass
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import JSONLoader

from openai import OpenAI

# Load the .env file
load_dotenv()

# Get the API key from the environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# If the API key is not set, ask the user to provide it
if not google_api_key:
    google_api_key = getpass.getpass("Provide your Google API Key")

# Using JSONLoader to load the data
loader = JSONLoader(
    file_path='cleaned_uvu-data-1.json',
    jq_schema='.[].html',
    text_content=False)

data = loader.load()

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model = "text-embedding-ada-002",
        input = [text]
    )
    
    return response.data[0].embedding

# Create the ChatGoogleGenerativeAI object
llm = ChatGoogleGenerativeAI(model="gemini-pro")

