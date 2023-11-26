import requests

def fetch_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    print(data)

fetch_data()
