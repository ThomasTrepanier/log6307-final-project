def hideEmail(email):
    #hide email
    text = re.sub(r'[^@.]', 'x', email)
    return text


with open('path/to/csvfile', 'r') as file:
     lines = [l.strip().split(';') for l in file.readlines()]

modifiedlines = []       # to store lines after email field is modified 

for i in lines[1:]:         # iterating from index 1 as index 0 is header
    i[3] = hideEmail(i[3])       # as email field is at index 3
    modifiedlines.append(';'.join(i))     # appending modified line

with open('path/to/csvfile', 'w') as file:
     file.writelines(modifiedlines)            # writing the lines back to file
