import re
import os

def read_markdown_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def extract_table(markdown_content):
    table_pattern = r'\|(.+)\|\n\|[-]+\|\n((?:\|.*\|\n)+)'
    matches = re.finditer(table_pattern, markdown_content, re.MULTILINE)
    tables = []

    for match in matches:
        header_row = match.group(1).strip().split('|')
        data_rows = match.group(2).strip().split('\n')

        table_data = []
        for row in data_rows:
            row_data = row.strip().split('|')
            table_data.append(dict(zip(header_row, row_data)))

        tables.append(table_data)

    return tables

def create_hugo_content(table_data, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for table in table_data:
        title = table.get('Title', 'Untitled')
        content = f"+++\ntitle = \"{title}\"\n+++\n\n"
        
        for key, value in table.items():
            if key != 'Title':
                content += f"{key}: {value}\n"

        filename = f"{title.lower().replace(' ', '-')}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    markdown_filename = 'input.md'  # Replace with your input Markdown file
    output_directory = 'hugo_content'  # Replace with your desired output directory

    markdown_content = read_markdown_file(markdown_filename)
    tables = extract_table(markdown_content)
    create_hugo_content(tables, output_directory)

if __name__ == "__main__":
    main()
