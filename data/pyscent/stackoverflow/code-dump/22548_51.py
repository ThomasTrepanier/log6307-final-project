def convert_what(numeral_sys_1, numeral_sys_2):

    l1 = [["Hexadecimal","Decimal"],["Hexadecimal","Binary"],
            ["Decimal","Hexadecimal"],["Decimal","Binary"],
            ["Binary","Hexadecimal"],["Binary","Decimal"]]

    return l1.index([numeral_sys_1, numeral_sys_2]) + 1 if [numeral_sys_1,numeral_sys_2] in l1 else 0
