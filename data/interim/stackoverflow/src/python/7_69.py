def substring(strings, final=None):
    if final is None: final = []
    for string in strings:
        while string:
            final.append(string)
            string = string[1:]
    return final
