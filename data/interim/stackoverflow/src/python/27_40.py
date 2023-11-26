import re

def hideEmail(email):
    #hide email
    text = re.sub(r'[^@.]', 'x', email)
    return text 

with open('file.csv', 'r') as r:
    r = map(hideEmail, r.readlines())

with open('file2.csv', 'w') as f:
    for line in r:
        f.write(line + '\n')
