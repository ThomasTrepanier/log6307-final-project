from itertools import zip_longest

def minmax(data):
    it = iter(data)
    _min = _max = next(it)
    for a, b in zip_longest(it, it, fillvalue=_min):
        if a > b:
            # swap items to make a <= b
            a, b = b, a
        if  a < _min:
            _min = a
        if b > _max:
            _max = b
    return _min, _max
