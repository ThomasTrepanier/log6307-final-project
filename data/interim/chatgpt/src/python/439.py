import tkinter as tk
import requests
import json

def fetch_country_data(country):
    response = requests.get(f'https://restcountries.eu/rest/v2/name/{country}')
    data = response.json()
    return data

def on_button_click():
    country = country_entry.get()
    data = fetch_country_data(country)
    text_box.insert('end', json.dumps(data[0], indent=2) + '\n')

window = tk.Tk()

country_entry = tk.Entry(window)
country_entry.pack()

text_box = tk.Text(window)
text_box.pack()

button = tk.Button(window, text="Fetch country data", command=on_button_click)
button.pack()

window.mainloop()
