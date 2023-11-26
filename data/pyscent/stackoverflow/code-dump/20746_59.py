def split_by_idx_sd(items, idx=1):
    result = {}
    for item in items:
        result.setdefault(item[idx], []).append(item)
    return result
