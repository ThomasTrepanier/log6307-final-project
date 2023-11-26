def extract_table(markdown_content):
    table_pattern = r'\|(.+)\|\n((?:.*\|\n)+)'
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
