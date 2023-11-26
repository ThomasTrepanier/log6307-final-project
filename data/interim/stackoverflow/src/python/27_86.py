from collections import OrderedDict


def nub(iterable):
    """Returns unique elements preserving order."""
    return OrderedDict.fromkeys(iterable).keys()
