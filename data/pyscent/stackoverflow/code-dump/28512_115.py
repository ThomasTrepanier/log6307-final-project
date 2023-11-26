from itertools import groupby

def getn(s):
    sections = groupby(s, key=lambda char: char.isdigit())
    result = []
    for isdig, chars in sections:
        if isdig:
            result += list(reversed(list(chars)))
        else:
            result += list(chars)
    return "".join(result)

input = "abc123abc456abc7891"
print(getn(input))
