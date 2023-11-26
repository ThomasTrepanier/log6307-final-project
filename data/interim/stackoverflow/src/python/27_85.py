from itertools import islice

def unique_everseen(iterable):
    seen = set()
    seen_add = seen.add
    for element in iterable:
        if element not in seen:
            seen_add(element)
            yield element

res = list(islice(unique_everseen(a), 5))  # [1, 2, 3, 4, 5]
