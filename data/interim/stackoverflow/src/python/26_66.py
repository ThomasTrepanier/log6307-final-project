def uniqueIndexes(l):
    seen = set()
    res = []
    for i, n in enumerate(l):
        if n not in seen:
            res.append(i)
            seen.add(n)
    return res

l=[1,2,2,3,4,5,5,5,2]

uniqueIndexes(l)
