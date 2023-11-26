import re
import json

def is_text(line):
    # returns True if line starts with a date and time in "YYYY-MM-DD HH:MM:SS" format
    line = line.lstrip('|') # you said some lines start with a leading |, remove it
    return re.match("^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})", line)

json_objects = []

with open("data.txt") as f:
    json_lines = []

    for line in f:
        if not is_text(line):
            json_lines.append(line)
        else:
            # if there's multiple text lines in a row json_lines will be empty
            if json_lines:
                json_objects.append(json.loads("".join(json_lines)))
                json_lines = []

    # we still need to parse the remaining object in json_lines
    # if the file doesn't end in a text line
    if json_lines:
        json_objects.append(json.loads("".join(json_lines)))

print(json_objects)
