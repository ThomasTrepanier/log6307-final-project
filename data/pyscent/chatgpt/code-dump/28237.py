#!/usr/bin/env python3

import os
import subprocess

def camel_to_snake(name):
    """Converts a camel case string to snake case."""
    result = ""
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result += "_"
        result += char.lower()
    return result

def git_mv(old_path, new_path):
    """Renames a file using 'git mv'."""
    subprocess.run(['git', 'mv', old_path, new_path])

def main():
    # Change directory to your codebase root folder
    os.chdir(os.path.join(os.environ['HOME'], 'src/temporalio/temporal'))

    # Loop through each file in the directory and its subdirectories
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.go') and any(c.islower() and c.isalpha() for c in file):
                old_path = os.path.join(root, file)
                new_name = camel_to_snake(file)
                new_path = os.path.join(root, new_name)

                # Rename the file using 'git mv'
                git_mv(old_path, new_path)
                print(f"Renamed {old_path} to {new_path}")

if __name__ == '__main__':
    main()
