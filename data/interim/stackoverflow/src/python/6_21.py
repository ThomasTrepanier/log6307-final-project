def counts(items):
    d = {}
    for item in items:
        d[item] = d.get(item, 0) + 1
    return d

counts(A) == counts(B)
