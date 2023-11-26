def update(d, key_lst , val):
    for k in key_lst[:-1]:
        if k not in d:
            d[k] = {}
        d = d[k]
    d[key_lst[-1]] = val

d = {}

update(d, list('qwer'), 0)
# d = {'q': {'w': {'e': {'r': 0}}}}
