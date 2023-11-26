def generate_bibtext(self, book):
    volume_info = book['volumeInfo']

    title = volume_info.get('title', '')
    authors = ' and '.join(volume_info.get('authors', ['']))
    publisher = volume_info.get('publisher', '')
    published_date = volume_info.get('publishedDate', '')
    pages = volume_info.get('pageCount', '')
    place = volume_info.get('place', '')  # Not all books will have this

    bibtext = f"@book{{googlebooks{book['id']},\n"
    bibtext += f" title={{ {title} }},\n"
    bibtext += f" author={{ {authors} }},\n"
    bibtext += f" year={{ {published_date} }},\n"
    bibtext += f" publisher={{ {publisher} }},\n"
    bibtext += f" pages={{ {pages} }},\n"
    bibtext += f" place={{ {place} }}\n"  # Include the place of publication
    bibtext += "}"

    return bibtext
