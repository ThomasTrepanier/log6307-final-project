def flatten(d, base=()):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from flatten(v, base + (k,))
        else:
            yield base + (k, v)
