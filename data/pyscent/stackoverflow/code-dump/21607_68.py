def substring(strings):
    final = []
    for string in strings:
        while string:
            final.append(string)
            string = string[1:]
    return final
