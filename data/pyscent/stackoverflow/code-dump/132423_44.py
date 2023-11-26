from itertools import repeat

def zip_by_first(*args, fillvalue=None):
    # zip_by_first('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    # zip_by_first('ABC', 'xyzw', fillvalue='-') --> Ax By Cz
    if not args:
        return
    iterators = [iter(it) for it in args]
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                if i == 0:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)
