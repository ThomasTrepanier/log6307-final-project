def substring(stringslist):
    final = []
    for string in stringslist:
        final.append(string)
        if len(string)==1:
            return final
        else:
            final.extend(substring([string[:-1]]))

    return final

