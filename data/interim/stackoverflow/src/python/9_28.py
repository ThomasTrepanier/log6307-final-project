import re

def is_broken(input_list, pattern = re.compile("(?:ab)*")):
    return pattern.fullmatch(''.join(input_list)) is None

print(is_broken(['a','b','a','b','a','b','a','b','a','b','a','b','a','b','a','b']))
print(is_broken(['a','b','b','a','a','b','a','b','a','a','a','b','a','b','b','a']))
