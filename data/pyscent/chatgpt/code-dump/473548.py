import argparse
import re
import os
import json

def read_config_file(config_filename):
    with open(config_filename, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

# ... (other functions remain the same)

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown table to Hugo content files")
    parser.add_argument("filename", help="Input Markdown file containing the table")
    parser.add_argument("--config", default="column_mapping.json", help="JSON configuration file for column mapping")
    args = parser.parse_args()

    output_directory = 'hugo_content'  # Replace with your desired output directory

    markdown_content = read_markdown_file(args.filename)
    tables = extract_table(markdown_content)
    config = read_config_file(args.config)
    column_mapping = config.get("column_mapping", {})
    
    create_hugo_content(tables, output_directory, column_mapping)

if __name__ == "__main__":
    main()
