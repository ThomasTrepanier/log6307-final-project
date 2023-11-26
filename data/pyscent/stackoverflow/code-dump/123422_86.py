from functools import partial

def reorder_from_idx(idx, a):
    return a[idx:] + a[:idx]

def cyclic_perm(a):
    return [partial(reorder_from_idx, i) for i in range(len(a))]


a = [1, 2, 3, 4, 5, 6]
result = cyclic_perm(a)
print(result)
#[functools.partial(<function reorder_from_idx at 0x00000298D92189D8>, 0),
# functools.partial(<function reorder_from_idx at 0x00000298D92189D8>, 1),
# functools.partial(<function reorder_from_idx at 0x00000298D92189D8>, 2),
# functools.partial(<function reorder_from_idx at 0x00000298D92189D8>, 3),
# functools.partial(<function reorder_from_idx at 0x00000298D92189D8>, 4),
# functools.partial(<function reorder_from_idx at 0x00000298D92189D8>, 5)]
result[3](a)
#[4, 5, 6, 1, 2, 3]
