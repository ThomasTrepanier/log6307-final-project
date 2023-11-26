import tkinter as tk
import requests
import json

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    weather = response.json()
    return weather

def on_button_click():
    city = city_entry.get()
    weather = get_weather(city, 'your_api_key')  # replace 'your_api_key' with the actual key
    text_box.insert('end', json.dumps(weather, indent=2))

window = tk.Tk()

city_entry = tk.Entry(window)
city_entry.pack()

text_box = tk.Text(window)
text_box.pack()

button = tk.Button(window, text="Get weather", command=on_button_click)
button.pack()

window.mainloop()
