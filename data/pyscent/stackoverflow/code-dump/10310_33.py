def get_keys_in_range(dct, lo=0, hi=100):
    rng = range(lo, hi) 
    for key, lst in dct.items():
        if any(l in rng for l in lst):
            yield key

[*get_keys_in_range(new_dict, lo=0, hi=100)]
# ['worry', 'win']
