def update_generate_statements(file_path):
    """Updates the go:generate statements in a Go source code file."""
    with open(file_path, 'r+') as file:
        content = file.read()

        # Match go:generate statements with mockgen command
        pattern = r'//go:generate\s+mockgen\s+.*-source\s+(\S+)\s+.*-destination\s+(\S+)\s*'
        matches = re.findall(pattern, content)

        if matches:
            for match in matches:
                old_source = match[0]
                new_source = camel_to_snake(old_source)
                old_destination = match[1]
                new_destination = camel_to_snake(old_destination)
                updated_content = content.replace(old_source, new_source).replace(old_destination, new_destination)
                file.seek(0)
                file.write(updated_content)
                file.truncate()
