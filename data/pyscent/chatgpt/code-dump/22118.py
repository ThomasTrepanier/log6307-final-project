import re
import sys

def update_file_header(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find the relevant lines in the file header
    for i, line in enumerate(lines):
        # Check for the end of the header
        if line.startswith('import'):
            end_of_header_index = i
            break

        # Extract the necessary info for the align import line
        if line.startswith('! This file was ported from'):
            source_module = line.split()[-1]
        elif line.startswith('!') and 'commit' in line:
            split_line = line.split()
            repo_ref = split_line[1]
            commit_id = split_line[-1]

    # Generate the new line
    new_line = f'#align_import {source_module} from "{repo_ref}"@"{commit_id}"\n'

    # Insert the new line after the header
    lines.insert(end_of_header_index, new_line)

    # Write the updated lines back to the file
    with open(file_path, 'w') as f:
        f.writelines(lines)

# The first command line argument is the file path
file_path = sys.argv[1]
update_file_header(file_path)
