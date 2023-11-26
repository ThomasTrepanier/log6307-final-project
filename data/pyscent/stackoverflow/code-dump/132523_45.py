def zip_first(a, b):
    ai, bi = iter(a), iter(b)
    while True:
        try:
            aa = next(ai)
        except StopIteration:
            return           
        try:
            bb = next(bi)
        except StopIteration:
            bb = None
        yield aa, bb
