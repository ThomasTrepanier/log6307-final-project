#!/usr/bin/env python3

import os
import re
import subprocess

def camel_to_snake(name):
    """Converts a camel case string to snake case."""
    name = name.replace("nDC", "ndc")

    result = ""
    prev_char = ""
    for char in name:
        if char.isupper() and prev_char.islower():
            result += "_" + char.lower()
        else:
            result += char.lower()
        prev_char = char
    return result

def git_mv(old_path, new_path):
    """Renames a file using 'git mv'."""
    subprocess.run(['git', 'mv', old_path, new_path])

def rename_file(old_path):
    """Renames a file using 'git mv' and updates go:generate statements."""
    base_name = os.path.basename(old_path)
    new_name = None

    if base_name.endswith("Test.go"):
        prefix = base_name[:-len("Test.go")]
        new_name = "test_" + camel_to_snake(prefix) + ".go"
    else:
        new_name = camel_to_snake(base_name)

    new_path = os.path.join(os.path.dirname(old_path), new_name)
    git_mv(old_path, new_path)
    print(f"Renamed {old_path} to {new_path}")

    update_generate_statements(new_path)
    print(f"Updated go:generate statements in {new_path}")

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
                rename_file(file_path)

if __name__ == '__main__':
    main()
