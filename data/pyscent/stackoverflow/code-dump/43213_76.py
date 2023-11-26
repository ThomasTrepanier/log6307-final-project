def normalise(value):
    if value.isalpha():
        return value
    if value.isnumeric():
        return int(value)
    return [int(i) for i in value.replace(",", "").split()]

def normalise_value(lst):
    xs = [[i] if isinstance(i, int) else i for i in lst]
    while len(xs) < 3:
        xs.append([])  # gets the empty list as needed
    return tuple(xs)

def strip_newline(string, newline="\n"):
    return string.replace(newline, "")
