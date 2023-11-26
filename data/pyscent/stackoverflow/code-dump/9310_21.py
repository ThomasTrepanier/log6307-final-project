def print_nested_keys(dic,path=''):
    for k,v in dic.items():
        if isinstance(v,dict):
            path+=k+"."
            yield from print_nested_keys(v,path)
        else:
            path+=k
            yield path
