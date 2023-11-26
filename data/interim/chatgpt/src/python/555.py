def create_hugo_content(tables, output_dir, column_mapping):
    os.makedirs(output_dir, exist_ok=True)

    for table in tables:
        for row in table:
            title_column = next((col for col in column_mapping if "title" in column_mapping[col].lower()), None)
            title = row.get(title_column)
            if title is None or title.strip() == "":
                title = "Untitled"
            
            content = f"+++\ntitle = \"{title}\"\n+++\n\n"

            for key, value in row.items():
                if key in column_mapping:
                    content += f"{column_mapping[key]}: {value}\n"

            filename = f"{title.lower().replace(' ', '-')}.md"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
