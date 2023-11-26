def full_format(i):
    # limit of first range is 26 letters (A-Z) times 999 numbers (001-999)
    if i < 26 * 999:
        c,n = divmod(i,999)   # quotient c is index of letter 0-25, remainder n is 0-998
        c = chr(ord('A') + c) # compute letter
        n += 1
        return f'{c}{n:03}'
    # After first range, second range is 26 letters times 26 letters * 99 numbers (01-99)
    elif i < 26*999 + 26*26*99:
        i -= 26*999               # remove first range offset
        cc,n = divmod(i,99)       # remainder n is 0-98, use quotient cc to compute two letters
        c1,c2 = divmod(cc,26)     # c1 is index of first letter, c2 is index of second letter
        c1 = chr(ord('A') + c1)   # compute first letter
        c2 = chr(ord('A') + c2)   # compute second letter
        n += 1
        return f'{c1}{c2}{n:02}'
    else:
        raise OverflowError(f'limit is {26*999+26*26*99}')

for i in range(92880, 92898):
    print(full_format(i))
