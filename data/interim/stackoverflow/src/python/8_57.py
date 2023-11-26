import re

with open('sample.txt') as f:
    data = f.read()

def replace(m):
    return ''.join([c if c.isspace() else '*'
                    for c in m.group(0)])

data = re.sub(r'quick\s+brown|over\s+the',replace,data)
print(data)
