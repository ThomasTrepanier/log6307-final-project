from itertools import chain

def rotate_values(my_dict):
    keys = iter(my_dict.keys())
    keys = chain(keys, [next(keys)])
    return dict(zip(keys, my_dict.values()))
