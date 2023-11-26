def func(x, y):
    if x[-1].islower():
        return x + y.upper()
    else:
        return x + y.lower()

new_s = reduce(func, s) # eXaMpLe
