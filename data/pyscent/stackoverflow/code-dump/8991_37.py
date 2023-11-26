from fractions import Fraction

def sqrt(x, n):
    x = x if isinstance(x, Fraction) else Fraction(x)
    upper = x + 1
    for i in range(0, n):
        upper = (upper + x/upper) / 2
    lower = x / upper
    if lower > upper:
        raise ValueError("Sanity check failed")
    return (lower, upper)
