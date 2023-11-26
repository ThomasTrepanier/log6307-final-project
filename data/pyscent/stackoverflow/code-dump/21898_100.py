from collections import OrderedDict

def f(x, a, b):
    print(x, a, b)

d = OrderedDict({'a': 3, 'b':4})
f(10, *d.values())
