import argparse
import re
import os

def read_markdown_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

# ... (rest of the functions remain the same)

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown table to Hugo content files")
    parser.add_argument("filename", help="Input Markdown file containing the table")
    args = parser.parse_args()

    output_directory = 'hugo_content'  # Replace with your desired output directory

    markdown_content = read_markdown_file(args.filename)
    tables = extract_table(markdown_content)
    create_hugo_content(tables, output_directory)

if __name__ == "__main__":
    main()
