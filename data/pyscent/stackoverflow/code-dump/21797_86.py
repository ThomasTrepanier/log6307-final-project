def auto_increment(number):
    if number == 'ZZZZ':
        return 'ZZZZ'

    digits = "".join([i for i in number if i.isdigit()])
    chars = "".join([i for i in number if not i.isdigit()])
    if int(digits) == int('9' * len(digits)):
        digits = "000"
        new_char = [ord(i) for i in chars]
        if new_char[-1] % ord('Z') == 0:
            new_char = "".join([chr(i) for i in new_char]) + 'A'
        else:
            new_char[-1] = new_char[-1] + 1
            new_char = "".join([chr(i) for i in new_char])
    else:
        new_char = chars

    new_digit = int(digits) + 1
    l = len(new_char) 
    ll = len(str(new_digit))
    new_digit = (("0" * (3-ll)) + str(new_digit))[(l-1):]
    return f"{new_char}{new_digit}"
