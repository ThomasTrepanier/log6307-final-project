def manual_replace(s, char, index):
    return s[:index] + char + s[index +1:]

string = '11234'
print(manual_replace(string, 'I', 0))
