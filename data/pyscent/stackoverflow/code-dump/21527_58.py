import re

def convert_commas(old):

    new = []
    pattern = re.compile(r"\d+,\d+")
    for word in old.split():
        if re.findall(pattern, word):
            word = word.replace(',','')
        new.append(word)

    new = (" ").join(new)
    return new

print(convert_commas(old))
