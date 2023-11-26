from collections import defaultdict

def heuristic(data, sort_data=False):
    data = sorted(data) if sort_data else data[:]
    out = [data.pop(0)]
    indexes = defaultdict(set)
    for i, triple in enumerate(data):
        for mark in enumerate(triple):
            indexes[mark].add(i)
    remain = set(range(len(data)))
    while remain:
        a, b, c = out[-1]
        best = 4, None
        for mark in enumerate(out[-1]):
            for i in indexes[mark]:
                x, y, z = data[i]
                candidate = (a != x) + (b != y) + (c != z), i
                if candidate < best:
                    best = candidate
        i = best[1]
        if i is None:
            i = min(remain)
        remain.remove(i)
        t = data[i]
        for pattern in enumerate(t):
            indexes[pattern].remove(i)
        out.append(t)
    return out
