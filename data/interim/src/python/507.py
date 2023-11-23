def generate_bibtext(self, book):
    volume_info = book['volumeInfo']

    title = volume_info.get('title', '')
    authors = ' and '.join(volume_info.get('authors', ['']))
    publisher = volume_info.get('publisher', '')
    published_date = volume_info.get('publishedDate', '')
    pages = volume_info.get('pageCount', '')
    url = book['selfLink']  # URL of the book on Google Books
    place = ''  # Place of publication is not available from the API

    bibtext = f"@book{{googlebooks{book['id']},\n"
    bibtext += f" title={{ {title} }},\n"
    bibtext += f" author={{ {authors} }},\n"
    bibtext += f" year={{ {published_date} }},\n"
    bibtext += f" publisher={{ {publisher} }},\n"
    bibtext += f" pages={{ {pages} }},\n"
    bibtext += f" url={{ {url} }},\n"  # Include the URL of the book on Google Books
    bibtext += f" place={{ {place} }}\n"  # Include the place of publication (if known)
    bibtext += "}"

    return bibtext
