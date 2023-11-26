def my_func(st):
    operations = (str.lower, str.upper)
    return ''.join(operations[i%2](x) for i, x in enumerate(st))

print(my_func('austin'))
# aUsTiN
