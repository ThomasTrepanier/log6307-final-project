ex_dict = {"milk":5, "eggs":2, "flour": 3}

def sum_rec(it):
    if isinstance(it, dict):
        it = iter(it.values())
    try:
        v = next(it)
    except StopIteration:
        return 0
    return v + sum_rec(it)

sum_rec(ex_dict)
# 10
