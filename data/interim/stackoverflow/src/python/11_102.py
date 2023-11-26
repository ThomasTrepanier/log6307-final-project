def string_skip(string):
    new_string = ""
    for i, n in enumerate(string):
        if i % 2 == 0:
            new_string += n

    return new_string
