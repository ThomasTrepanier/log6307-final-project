l = [3, 22, 10, 15, 32, 10, 5]


def f(ml: list):
    a = []
    for i1 in ml:
        for i2 in ml:
            if not i1 + i2 in a:
                a.append(i1 + i2)
    return a


print(f(l))

