def update_generate_statements(file_path):
    """Updates the go:generate statements in a Go source code file."""
    with open(file_path, 'r+') as file:
        content = file.read()

        # Match go:generate statements
        pattern = r'(?m)^//go:generate\s+(.*)$'
        matches = re.findall(pattern, content)

        if matches:
            for match in matches:
                generate_line = match
                updated_line = generate_line

                # Find Go source code file names on the line
                file_names = re.findall(r'\b(\w+\.go)\b', generate_line)
                if file_names:
                    for old_name in file_names:
                        new_name = camel_to_snake(old_name)
                        updated_line = updated_line.replace(old_name, new_name)

                # Replace the go:generate line with the updated one
                updated_content = content.replace(generate_line, updated_line)
                file.seek(0)
                file.write(updated_content)
                file.truncate()
