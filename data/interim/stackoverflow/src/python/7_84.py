def excel_format(num):
    # see https://stackoverflow.com/a/182924/1639625
    res = ""
    while num:
        mod = (num - 1) % 26
        res = chr(65 + mod) + res
        num = (num - mod) // 26
    return res

def full_format(num, d=3):
    chars = num // (10**d-1) + 1 # this becomes   A..ZZZ
    digit = num %  (10**d-1) + 1 # this becomes 001..999
    return excel_format(chars) + "{:0{}d}".format(digit, d)

for i in range(10000):
    print(i, full_format(i, d=2))
