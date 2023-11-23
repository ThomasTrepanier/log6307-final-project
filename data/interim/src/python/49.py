def camel_to_snake(name):
    """Converts a camel case string to snake case."""
    result = ""
    prev_char = ""
    for char in name:
        if char.isupper() and prev_char.islower():
            result += "_" + char.lower()
        else:
            result += char.lower()
        prev_char = char
    return result
