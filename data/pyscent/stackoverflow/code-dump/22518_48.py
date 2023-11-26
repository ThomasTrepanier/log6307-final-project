def convert_what(numeral_sys_1, numeral_sys_2):
    numeral_dict = {
        ("Hexadecimal", "Decimal"    ) : 1,
        ("Hexadecimal", "Binary"     ) : 2,
        ("Decimal",     "Hexadecimal") : 4, 
        ("Decimal",     "Binary"     ) : 6,
        ("Binary",      "Hexadecimal") : 5,
        ("Binary",      "Decimal"    ) : 3
    }
    return numeral_dict.get((numeral_sys_1, numeral_sys_2), 0)
