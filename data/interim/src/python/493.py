import tkinter as tk
import requests

def fetch_book_data(query):
    params = {'q': query}
    response = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)
    data = response.json()
    return data

def on_button_click():
    query = query_entry.get()
    data = fetch_book_data(query)

    # Clear the listbox and the text widget
    list_box.delete(0, 'end')
    description_text.delete('1.0', 'end')

    # Update the label with the total number of books
    total_books.set(f"Total books found: {data['totalItems']}")

    # Populate the listbox with the titles of the books
    for item in data['items']:
        title = item['volumeInfo'].get('title', 'No title available')
        list_box.insert('end', title)
        books_data[title] = item['volumeInfo'].get('description', 'No description available')

def on_listbox_select(event):
    # Get the currently selected book title
    title = list_box.get(list_box.curselection())

    # Clear the text widget
    description_text.delete('1.0', 'end')

    # Display the description of the selected book
    description_text.insert('end', books_data[title])

window = tk.Tk()

query_entry = tk.Entry(window)
query_entry.pack()

total_books = tk.StringVar()
total_books_label = tk.Label(window, textvariable=total_books)
total_books_label.pack()

list_box = tk.Listbox(window)
list_box.pack()
list_box.bind('<<ListboxSelect>>', on_listbox_select)

description_text = tk.Text(window)
description_text.pack()

button = tk.Button(window, text="Fetch book data", command=on_button_click)
button.pack()

# A dictionary to store the descriptions of the books
books_data = {}

window.mainloop()
