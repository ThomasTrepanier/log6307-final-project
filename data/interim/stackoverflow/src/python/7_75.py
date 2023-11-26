lst=['house','cat','dog']

def substring(string, reversed=False):
    if string:  # if string is not zero-length:
        yield string  # yield its full length
        yield from substring(string[:-1] if reversed else string[1:])  # and recurse

def substrings(stringslist, reversed=False):
    for string in stringslist:
        yield from substring(string, reversed)
