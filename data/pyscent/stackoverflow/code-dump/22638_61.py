def convert_what(numeral_sys_1, numeral_sys_2):

    num = ['Hexadecimal','Decimal','Binary']
    tbl = [[0,1,2],
           [4,0,6],
           [5,3,0]]
    try:
        return tbl[num.index(numeral_sys_1)][num.index(numeral_sys_2)]
    except ValueError:
        return 0
