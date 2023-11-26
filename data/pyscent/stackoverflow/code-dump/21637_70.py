def substring(strings, final=None):
    if final is None: final = []
    # base case: empty list
    if not strings: return final
    # recursive case:
    # work on first string in list
    string = strings[0]
    # add all substrings to final
    while string:
        final.append(string)
        string = string[1:]
    return substring(strings[1:], final)
