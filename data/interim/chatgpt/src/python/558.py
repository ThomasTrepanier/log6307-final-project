import argparse
import os
import json

def read_config_file(config_filename):
    with open(config_filename, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

def read_markdown_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def create_hugo_content(table_data, output_dir, column_mapping):
    os.makedirs(output_dir, exist_ok=True)

    for row in table_data:
        title_column = next((col for col in column_mapping if "title" in column_mapping[col].lower()), None)
        title = row[title_column] if title_column in row else 'Untitled'
        
        content = f"+++\ntitle = \"{title}\"\n+++\n\n"

        for key, value in row.items():
            if key in column_mapping:
                content += f"{column_mapping[key]}: {value}\n"

        filename = f"{title.lower().replace(' ', '-')}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown table to Hugo content files")
    parser.add_argument("filename", help="Input Markdown file containing the table")
    parser.add_argument("--config", default="column_mapping.json", help="JSON configuration file for column mapping (default: column_mapping.json)")
    args = parser.parse_args()

    output_directory = 'hugo_content'  # Replace with your desired output directory

    markdown_content = read_markdown_file(args.filename)
    rows = markdown_content.strip().split('\n')
    column_names = rows[0].strip().split('|')

    table_data = []
    for row in rows[1:]:
        row_values = row.strip().split('|')
        row_data = {col_name.strip(): value.strip() for col_name, value in zip(column_names, row_values)}
        table_data.append(row_data)

    config = read_config_file(args.config)
    column_mapping = config.get("column_mapping", {})

    create_hugo_content(table_data, output_directory, column_mapping)

if __name__ == "__main__":
    main()
