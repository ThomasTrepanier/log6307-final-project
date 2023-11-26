from collections import defaultdict

nest = lambda: defaultdict(nest)
d = nest()

def update(d, key_lst , val):
    for k in key_lst[:-1]:
        d = d[k]
    d[key_lst[-1]] = val

update(d, 'qwer', 0)
