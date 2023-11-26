def chunks_by_size(items, max_size, get_size=len):
    result = []
    size = max_size + 1
    for item in items:
        item_size = get_size(item)
        size += item_size
        if size > max_size:
            result.append([])
            size = item_size
        result[-1].append(item)
    return result
