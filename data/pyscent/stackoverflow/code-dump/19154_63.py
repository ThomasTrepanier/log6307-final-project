ex_dict = {"milk":5, "eggs":2, "flour": 3}

def sum_rec(d):
    try:
        k,v = d.popitem()
    except KeyError:
        return 0
    return v + sum_rec(d)

sum_rec(ex_dict)
# 10
