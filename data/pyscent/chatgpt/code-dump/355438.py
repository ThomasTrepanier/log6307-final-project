import tkinter as tk
import requests
import json

def fetch_data():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = response.json()
    return data

def on_button_click():
    data = fetch_data()
    for user in data:
        text_box.insert('end', json.dumps(user, indent=2) + '\n')

window = tk.Tk()

text_box = tk.Text(window)
text_box.pack()

button = tk.Button(window, text="Fetch users", command=on_button_click)
button.pack()

window.mainloop()
