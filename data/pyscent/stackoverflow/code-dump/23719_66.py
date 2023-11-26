def partition(L, key=None):

    if key is None:
        key = lambda x: x

    parts = []
    for item in L:
        for part in parts:
            if key(item) == key(part[0]):
               part.append(item)
               break
        else:
            parts.append([item])
    return parts

def unique(L, key=None):
    return [p[0] for p in partition(L, key=key)]

alist = [["A"], ["B"], ["A","B"], ["B","A"], ["A","B","C"], ["B", "A", "C"]]

unique(alist)
# results in [['A'], ['B'], ['A', 'B'], ['B', 'A'], ['A', 'B', 'C'], ['B', 'A', 'C']]

unique(alist, key=lambda v: tuple(sorted(v)))
# results in [['A'], ['B'], ['A', 'B'], ['A', 'B', 'C']]
