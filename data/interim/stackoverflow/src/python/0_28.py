import itertools

def all_equal(iterable):
    "Returns True if all elements are equal"
    g = itertools.groupby(iterable)
    next(g, None)
    try:
        return not next(g, False)
    except TypeError:  # pd.NA next to a different value?
        return False

all_equal(df.counts)
