import tkinter as tk
import requests
import json

def get_cat_fact():
    response = requests.get('https://cat-fact.herokuapp.com/facts/random')
    fact = response.json()
    return fact

def on_button_click():
    fact = get_cat_fact()
    text_box.insert('end', json.dumps(fact, indent=2) + '\n')

window = tk.Tk()

text_box = tk.Text(window)
text_box.pack()

button = tk.Button(window, text="Get cat fact", command=on_button_click)
button.pack()

window.mainloop()
