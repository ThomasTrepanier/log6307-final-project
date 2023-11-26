def extract_table(markdown_content):
    lines = markdown_content.split('\n')
    tables = []
    table_start = None

    for idx, line in enumerate(lines):
        if table_start is None and re.match(r'\|[-]+\|$', line):
            table_start = idx + 1
        elif table_start is not None and re.match(r'\|[-]+\|$', line):
            table_data = lines[table_start:idx]
            tables.append(table_data)
            table_start = None

    return tables
