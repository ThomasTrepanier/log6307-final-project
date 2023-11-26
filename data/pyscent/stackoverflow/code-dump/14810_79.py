def make_hashable(o):
    if isinstance(o, dict):
        return frozenset((k, make_hashable(v)) for k, v in o.items())
    elif isinstance(o, list):
        return tuple(make_hashable(elem) for elem in o)
    elif isinstance(o, set):
        return frozenset(make_hashable(elem) for elem in o)
    else:
        return o
