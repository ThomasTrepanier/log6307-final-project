def string_skip(string):
    new_string = ""
    iterator = iter(string)
    for letter in iterator:
        new_string += letter
        next(iterator)
    return new_string
