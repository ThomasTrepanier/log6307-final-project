import requests
from bs4 import BeautifulSoup

def find_document_source(unique_phrase):
    # Replace 'YOUR_SEARCH_ENGINE_API_KEY' with an actual search engine API key
    search_engine_api_key = 'YOUR_SEARCH_ENGINE_API_KEY'
    search_engine_cx = 'YOUR_SEARCH_ENGINE_CUSTOM_SEARCH_ID'
    
    base_url = f'https://www.googleapis.com/customsearch/v1'
    query_params = {
        'key': search_engine_api_key,
        'cx': search_engine_cx,
        'q': unique_phrase
    }
    
    response = requests.get(base_url, params=query_params)
    results = response.json().get('items', [])
    
    for result in results:
        print("Title:", result['title'])
        print("Link:", result['link'])
        print("Description:", result['snippet'])
        print("="*50)

if __name__ == "__main__":
    unique_phrase = input("Enter the unique phrase from the document: ")
    find_document_source(unique_phrase)
