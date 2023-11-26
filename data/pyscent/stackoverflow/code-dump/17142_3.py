lst = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]


def split(i):
    if isinstance(i, list):
        return [split(v) for v in i]
    else:
        return [i]


print(split(lst))
