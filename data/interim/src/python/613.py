def create_hugo_content(tables, output_dir, column_mapping):
    os.makedirs(output_dir, exist_ok=True)

    for table_lines in tables:
        header_row = table_lines[0].strip().split('|')
        table_data = []

        for row_line in table_lines[2:]:
            row_data = row_line.strip().split('|')
            table_data.append(dict(zip(header_row, row_data)))

        title_column = next((col for col in column_mapping if "title" in column_mapping[col].lower()), None)
        title = table_data[0].get(title_column, 'Untitled')

        content = f"+++\ntitle = \"{title}\"\n+++\n\n"

        for row in table_data:
            for key, value in row.items():
                if key in column_mapping:
                    content += f"{column_mapping[key]}: {value}\n"

        filename = f"{title.lower().replace(' ', '-')}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
