def nub(iterable):
    seen = set()
    add_seen = seen.add
    for element in iterable:
        if element in seen:
            continue
        yield element
        add_seen(element)
