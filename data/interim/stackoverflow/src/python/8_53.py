def convert(key1, key2):
    keys = ["Hexadecimal", "Decimal", "Binary"]
    combinations = {(0, 1): 1, (0, 2): 2, (1, 0): 4, (1, 2): 6, (2, 0): 5, (2, 1): 3} # use keys indexes to map to combinations
    try:
        return combinations[(keys.index(key1), keys.index(key2))]
    except (KeyError, ValueError): # if value is not in list, return as 0
        return 0
