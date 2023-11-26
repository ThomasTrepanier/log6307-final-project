import collections


def split_by_idx_dd(items, idx=1):
    result = collections.defaultdict(list)
    for item in items:
        result[item[idx]].append(item)
    return result
