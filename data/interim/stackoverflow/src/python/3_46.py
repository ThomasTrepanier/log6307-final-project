def hill(lst):
    lst = lst.copy()
    last = cur = float('-inf')
    while lst and last <= cur:
        last, cur = cur, lst.pop()
    while lst and last >= cur:
        last, cur = cur, lst.pop()
    return not lst


def valley(lst):
    lst = lst.copy()
    last = cur = float('inf')
    while lst and last >= cur:
        last, cur = cur, lst.pop()
    while lst and last <= cur:
        last, cur = cur, lst.pop()
    return not lst
