def split_by_idx(items, idx=1):
    result = {}
    for item in items:
        key = item[idx]
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result
