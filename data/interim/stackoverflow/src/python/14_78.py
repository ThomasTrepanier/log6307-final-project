def flatten(d, base=(), depth=None):
    for k, v in d.items():
        if not isinstance(v, dict):
            yield base + (k, v)
        else:
            if depth is None:
                yield from flatten(v, base + (k,))
            else:
                if depth == 0:
                    yield base + (k, v)
                else:
                    yield from flatten(v, base + (k,), depth - 1)
