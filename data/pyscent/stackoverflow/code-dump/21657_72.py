def substring(strings, final=None):
    if final is None: final = []
    if not strings: return final
    if not string[0]: return substring(strings[1:], final)
    final.append(string)
    strings[0] = string[0][1:]
    return substring(strings, final)
