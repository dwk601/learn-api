import json
import html
import string
import re
from bs4 import BeautifulSoup

# Load the data from the JSON file
with open('uvu-data-1.json', 'r') as f:
    data = json.load(f)

# Clean the data
for item in data:
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(item['html'], 'html.parser')

    # Remove any script or style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Get the text from the parsed HTML
    text = soup.get_text()

    # Replace multiple newlines with a single newline
    text = '\n'.join(line for line in text.split('\n') if line.strip())

    # Unescape HTML entities
    text = html.unescape(text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Convert to lowercase
    text = text.lower()

    # Additional cleaning: Remove any non-alphanumeric characters and extra whitespace
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = ' '.join(text.split())

    # Update the 'html' field with the cleaned text
    item['html'] = text

# Save the cleaned data to a new JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)