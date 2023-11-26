def chunks_by_size_reduce(items, size, get_size=len):
    return functools.reduce(
        lambda a, b, size=size:
            a[-1].append(b) or a
            if a and sum(get_size(x) for x in a[-1]) + get_size(b) <= size
            else a.append([b]) or a, items, [])
