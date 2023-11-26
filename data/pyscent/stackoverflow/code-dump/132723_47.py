from itertools import zip_longest

def zip_first(a, b):
    z = zip_longest(a, b)
    for i, r in zip(range(len(a)), z):
        yield r
