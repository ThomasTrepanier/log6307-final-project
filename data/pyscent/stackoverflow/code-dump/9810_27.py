def minmax(ls):
    if len(ls) == 0:
        return None, None # or some default val
    mini = maxi = ls[0]
    for val in ls[1:]:
        if val < mini:
            mini = val
        elif val > maxi:
            maxi = val
    return mini, maxi
