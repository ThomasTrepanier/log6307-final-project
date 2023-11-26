def parse_dict_multikey(s):
    p = ast.parse(s)
    exp_dict = p.body[0].value
    keys = list(map(ast.literal_eval, exp_dict.keys))
    values = list(map(ast.literal_eval, exp_dict.values))
    c = Counter(keys)
    d = {}
    for k, v in zip(keys, values):
        if c[k] > 1:
            d.setdefault(k, []).append(v)
        else:
            d[k] = v
    return d
