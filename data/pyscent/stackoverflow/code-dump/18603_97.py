from operator import itemgetter

getters = [itemgetter(slice(i, i + 2)) for i in range(0, len(my_list), 2)]
vals = [g(my_list) for g in getters]


def score_vals(s):
    k, v = s
    return {'value': k, 'score': v}

list(map(score_vals, vals))
