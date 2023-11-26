from itertools import chain

def is_duplicated_value(d):
    flat = list(chain.from_iterable(nested_values(d)))
    return len(flat) != len(set(flat))
