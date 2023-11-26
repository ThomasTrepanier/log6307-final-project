def make_hashable(o):
    t = type(o)
    if isinstance(o, dict):
        o = frozenset((k, make_hashable(v)) for k, v in o.items())
    elif isinstance(o, list):
        o = tuple(make_hashable(elem) for elem in o)
    elif isinstance(o, set):
        o = frozenset(make_hashable(elem) for elem in o)
    return t, o
