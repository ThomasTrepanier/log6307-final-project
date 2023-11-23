import random
import re
import requests
from bs4 import BeautifulSoup

def find_document_source(unique_phrases):
    # Replace 'YOUR_SEARCH_ENGINE_API_KEY' with an actual search engine API key
    search_engine_api_key = 'YOUR_SEARCH_ENGINE_API_KEY'
    search_engine_cx = 'YOUR_SEARCH_ENGINE_CUSTOM_SEARCH_ID'
    
    base_url = f'https://www.googleapis.com/customsearch/v1'
    
    for phrase in unique_phrases:
        query_params = {
            'key': search_engine_api_key,
            'cx': search_engine_cx,
            'q': phrase
        }
        
        response = requests.get(base_url, params=query_params)
        results = response.json().get('items', [])
        
        print("Search phrase:", phrase)
        
        for result in results:
            print("Title:", result['title'])
            print("Link:", result['link'])
            print("Description:", result['snippet'])
            print("="*50)
            
def generate_unique_phrases(document, num_phrases=3, phrase_length=8):
    # Tokenize the document into words
    words = re.findall(r'\w+', document)
    
    # Generate unique phrases
    unique_phrases = set()
    while len(unique_phrases) < num_phrases:
        start_index = random.randint(0, len(words) - phrase_length)
        phrase = ' '.join(words[start_index:start_index + phrase_length])
        unique_phrases.add(phrase)
    
    return list(unique_phrases)

if __name__ == "__main__":
    # Read the document from a file or other source
    document = """
    This is the content of the document you want to identify the source for. Replace this with your actual document content.
    """
    
    unique_phrases = generate_unique_phrases(document)
    find_document_source(unique_phrases)
