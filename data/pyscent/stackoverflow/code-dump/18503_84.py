def hillorvalley(seq):
    is_dec, is_inc = False, False
    inflections = 0
    for i in range(len(seq)-1):
        if inflections > 1:
            # Early stop if more than 1 inflection
            return False
        right = seq[i+1]
        middle = seq[i]
        diff = right - middle
        if diff > 0:
            if is_dec:
                inflections += 1
            is_inc = True
            is_dec = False
        elif diff < 0:
            if is_inc:
                inflections += 1
            is_dec = True
            is_inc = False
    if inflections == 1:
        return True
    return False

assert hillorvalley([1, 1, 1, 1, 1]) is False
assert hillorvalley([1, 1]) is False
assert hillorvalley([1]) is False
assert hillorvalley([1, 2, 3, 5, 4]) is True
assert hillorvalley([5, 4, 1, 2, 3]) is True
assert hillorvalley([1, 2, 3, 5, 5]) is False
assert hillorvalley([9, 5, 4, -1, -2, 3, 7]) is True
assert hillorvalley([1, 2, 3, 5, 4, 3, 2, 1]) is True
assert hillorvalley([9, -1, 4, -1, -2, 3]) is False
