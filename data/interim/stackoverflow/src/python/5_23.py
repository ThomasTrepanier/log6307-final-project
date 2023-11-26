def rev_keys(d: dict) -> dict:
    '''Return dictionary structure with the 
        keys reasigned in opposite order'''
    old_keys = list(d.keys())
    new_keys = old_keys[::-1]
    nd = {}
    for ki in range(len(new_keys)):
        nd[new_keys[ki]]= d[old_keys[ki]]
    return nd
