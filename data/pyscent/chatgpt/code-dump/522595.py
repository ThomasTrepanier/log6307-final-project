import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

# Sanitize file paths for Windows
def sanitize_filepath(filepath):
    return re.sub(r'[<>:"/\\|?*]', '_', filepath)

# Download image from a URL
def download_image(url):
    img_data = requests.get(url).content
    filename = os.path.basename(unquote(url))
    sanitized_filename = sanitize_filepath(filename)
    local_filepath = os.path.join('./images', sanitized_filename)
    
    with open(local_filepath, 'wb') as img_file:
        img_file.write(img_data)
    
    return local_filepath

# Update HTML files
def update_html(file_content):
    soup = BeautifulSoup(file_content, 'html.parser')
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url:
            local_filepath = download_image(img_url)
            img_tag['src'] = local_filepath
    
    return str(soup)

# Update Markdown files
def update_markdown(file_content):
    pattern = r'!\[.*?\]\((.*?)\)'
    matches = re.findall(pattern, file_content)
    for img_url in matches:
        local_filepath = download_image(img_url)
        # Replace image URLs with local file paths in HTML format for GitHub compatibility
        file_content = file_content.replace(img_url, f'<img src="{local_filepath}" />')
    
    return file_content

# Main function
def update_file(filepath):
    if not os.path.exists('./images'):
        os.mkdir('./images')
    
    with open(filepath, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Identify file type and update accordingly
    if filepath.endswith('.html'):
        updated_content = update_html(file_content)
    elif filepath.endswith('.md'):
        updated_content = update_markdown(file_content)
    else:
        print('Unsupported file type.')
        return

    # Save the updated content back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Example usage
update_file('example.html')
update_file('example.md')
