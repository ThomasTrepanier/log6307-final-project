def substring(strings, final=None):
    if final is None: final = []
    if not strings: return final
    string = strings[0]
    if not string: return substring(strings[1:], final)
    final.append(string)
    strings[0] = string[1:]
    return substring(strings, final)
