def return_bound(x, l, h):
    low = abs(x - l)
    high = abs(x - h)
    if low < high:
        return l
    else:
        return h
