def f1(words):
    c = Counter()
    for word in words:
        c.update(set(word.lower()))
    return c

def f2(words):
    return Counter(
        c
        for word in words
        for c in set(word.lower()))

def f3(words):
    d = {}
    for word in words:
        for i in set(word.lower()):
            d[i] = d.get(i, 0) + 1
    return d
