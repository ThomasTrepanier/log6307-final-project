mapping = {
    'Hexadecimal': {'Decimal': 1, 'Binary': 2},
    'Binary': {'Decimal': 3, 'Hexadecimal': 5},
    'Decimal': {'Hexadecimal': 4, 'Binary': 6}
}
def convert_what(numeral_sys_1, numeral_sys_2):
    return mapping.get(numeral_sys_1, {}).get(numeral_sys_2, 0)
