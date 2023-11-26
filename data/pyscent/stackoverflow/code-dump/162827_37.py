def two_string(a, b):
    res = []
    i = 0
    for c in a:
        if c in b and i == b.index(c):
            res.append((c,i))
        i += 1
    print(res)
