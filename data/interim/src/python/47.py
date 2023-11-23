#!/usr/bin/env python3

import os
import re

def camel_to_snake(name):
    """Converts a camel case string to snake case."""
    result = ""
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result += "_"
        result += char.lower()
    return result

def update_generate_statements(file_path):
    """Updates the go:generate statements in a Go source code file."""
    with open(file_path, 'r+') as file:
        content = file.read()

        # Match go:generate statements with mockgen command
        pattern = r'//go:generate\s+mockgen\s+.*-destination\s+(\S+)\s*'
        matches = re.findall(pattern, content)

        if matches:
            for match in matches:
                old_path = match
                new_path = camel_to_snake(match)
                updated_content = content.replace(old_path, new_path)
                file.seek(0)
                file.write(updated_content)
                file.truncate()

def main():
    # Change directory to your codebase root folder
    os.chdir(os.path.join(os.environ['HOME'], 'src/temporalio/temporal'))

    # Loop through each file in the directory and its subdirectories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.go'):
                file_path = os.path.join(root, file)
                update_generate_statements(file_path)
                print(f"Updated go:generate statements in {file_path}")

if __name__ == '__main__':
    main()
