def convert_what_2(numeral_sys_1, numeral_sys_2):
    num_sys = ["Hexadecimal", "Decimal", "Binary"]
    r_value = {0: {1: 1, 2: 2},
               1: {0: 4, 2: 6},
               2: {0: 5, 1: 3} }
    try:
        value = r_value[num_sys.index(numeral_sys_1)][num_sys.index(numeral_sys_2)]
    except KeyError: # Catches when they are equal or undefined
        value = 0
    return value
