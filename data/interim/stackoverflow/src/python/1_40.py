from math import isqrt

def str_sqrt(num, digits):
    """ Arbitrary precision square root

        num arg must be a string
        Return a string with `digits` after
        the decimal point

        Written by PM 2Ring 2022.01.26
    """

    int_part , _, frac_part = num.partition('.')
    num = int_part + frac_part

    # Determine the required precision
    width = 2 * digits - len(frac_part)

    # Truncate or pad with zeroes
    num = num[:width] if width < 0 else num + '0' * width
    s = str(isqrt(int(num)))

    if digits:
        # Pad, if necessary
        s = '0' * (1 + digits - len(s)) + s
        s = f"{s[:-digits]}.{s[-digits:]}"
    return s
