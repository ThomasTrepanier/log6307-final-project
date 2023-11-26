from itertools import chain


def merge(*dicts):
    return dict(chain.from_iterable(d.items() for d in dicts))
