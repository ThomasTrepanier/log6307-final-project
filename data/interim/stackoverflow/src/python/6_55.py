def gen_dict(d, level=0):
    if level >= len(d):
        return 0
    key = tuple(d.keys())[level]
    return {val: gen_dict(d, level+1) for val in d.get(key)}

gen_dict(d)
