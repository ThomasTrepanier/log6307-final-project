import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

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
    book_cover_label.configure(image='')

    # Update the label with the total number of books
    total_books.set(f"Total books found: {data['totalItems']}")

    # Populate the listbox with the titles and authors of the books
    for item in data['items']:
        title = item['volumeInfo'].get('title', 'No title available')
        authors = ', '.join(item['volumeInfo'].get('authors', ['No authors available']))
        list_box.insert('end', f'{title} by {authors}')
        books_data[f'{title} by {authors}'] = (item['volumeInfo'].get('description', 'No description available'), item['volumeInfo'].get('imageLinks', {}).get('thumbnail'))

def on_listbox_select(event):
    # Get the currently selected book title
    title = list_box.get(list_box.curselection())

    # Clear the text widget and image label
    description_text.delete('1.0', 'end')
    book_cover_label.configure(image='')

    # Display the description and image of the selected book
    description, image_url = books_data[title]
    description_text.insert('end', description)

    if image_url:
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            photo = ImageTk.PhotoImage(image)
            book_cover_label.image = photo
            book_cover_label.configure(image=photo)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load book image: {e}")

window = tk.Tk()

query_entry = tk.Entry(window)
query_entry.pack(fill=tk.BOTH, expand=1)

total_books = tk.StringVar()
total_books_label = tk.Label(window, textvariable=total_books)
total_books_label.pack(fill=tk.BOTH, expand=1)

list_box = tk.Listbox(window)
list_box.pack(fill=tk.BOTH, expand=1)
list_box.bind('<<ListboxSelect>>', on_listbox_select)

description_text = tk.Text(window)
description_text.pack(fill=tk.BOTH, expand=1)

book_cover_label = tk.Label(window)
book_cover_label.pack(fill=tk.BOTH, expand=1)

button = tk.Button(window, text="Fetch book data", command=on_button_click)
button.pack(fill=tk.BOTH, expand=1)

# A dictionary to store the descriptions and image URLs of the books
books_data = {}

window.mainloop()
