import tkinter as tk
import requests

def fetch_dog_image():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json()['message']
    return image_url

def on_button_click():
    image_url = fetch_dog_image()
    text_box.insert('end', image_url + '\n')

window = tk.Tk()

text_box = tk.Text(window)
text_box.pack()

button = tk.Button(window, text="
