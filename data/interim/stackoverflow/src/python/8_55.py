def convert_what(numeral_sys_1, numeral_sys_2):
    return {
        ("Hexadecimal", "Decimal") : 1, 
        ("Hexadecimal", "Binary") : 2, 
        ("Binary", "Decimal") : 3,
        ("Decimal", "Hexadecimal") : 4,
        ("Binary", "Hexadecimal") : 5, 
        ("Decimal", "Binary") : 6, 
     }.get((numeral_sys_1, numeral_sys_2), 0)
