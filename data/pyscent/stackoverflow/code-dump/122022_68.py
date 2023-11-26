import re

def substring_length(string, char):
    match = re.search(f'{char}.+{char}', string)
    match_length = len(match.group(0)) if match else 0
    return match_length
