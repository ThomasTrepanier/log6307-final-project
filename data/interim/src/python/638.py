import random
import re
import requests

def find_document_source(unique_phrases):
    # ... (same as before) ...
    high_probability_source = get_high_probability_source(results)
    print("High Probability Source:")
    print("Title:", high_probability_source['title'])
    print("Link:", high_probability_source['link'])
    print("Description:", high_probability_source['snippet'])

def get_high_probability_source(results):
    # Count the frequency of each link
    link_frequency = {}
    for result in results:
        link = result['link']
        link_frequency[link] = link_frequency.get(link, 0) + 1
    
    # Find the link with the highest frequency
    high_frequency_link = max(link_frequency, key=link_frequency.get)
    
    # Find the result associated with the high frequency link
    high_probability_source = next(result for result in results if result['link'] == high_frequency_link)
    
    return high_probability_source

# Rest of the code remains the same
