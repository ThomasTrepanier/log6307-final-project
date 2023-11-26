def unique_everseen_limit(iterable, limit=5):
    seen = set()
    seen_add = seen.add
    for element in iterable:
        if element not in seen:
            seen_add(element)
            yield element
        if len(seen) == limit:
            break

a = [1,2,2,3,3,4,5,6]

res = list(unique_everseen_limit(a))  # [1, 2, 3, 4, 5]
