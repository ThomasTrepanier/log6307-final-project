import tkinter as tk
import requests
import json

def fetch_book_data(query):
    params = {'q': query}
    response = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)
    data = response.json()
    return data

def on_button_click():
    query = query_entry.get()
    data = fetch_book_data(query)
    for item in data['items']:
        text_box.insert('end', json.dumps(item['volumeInfo'], indent=2) + '\n')

window = tk.Tk()

query_entry = tk.Entry(window)
query_entry.pack()

text_box = tk.Text(window)
text_box.pack()

button = tk.Button(window, text="Fetch book data", command=on_button_click)
button.pack()

window.mainloop()
