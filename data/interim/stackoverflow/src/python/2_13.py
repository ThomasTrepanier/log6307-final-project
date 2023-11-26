def parse_dict(d):
    new_dict = {}
    for key,val in d.items():
        if isinstance(val,list):
            new_dict.update({f'{key}_{i+1}':v for i,v in enumerate(val)})
        else:
            new_dict[key] = val
    return new_dict

result = [parse_dict(d) for d in p]
