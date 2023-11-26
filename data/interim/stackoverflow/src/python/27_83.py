from itertools import groupby, islice

def first_unique(data, upper):
    return islice((key for (key, _) in groupby(data)), 0, upper)

a = [1, 2, 2, 3, 3, 4, 5, 6]

print(list(first_unique(a, 5)))
