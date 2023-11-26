def stop_at_four(lst):
    if 4 not in lst:
        return lst
    idx = 0
    accum_list = []
    while lst[idx] != 4:
        accum_list.append(lst[idx])
        idx += 1
    return accum_list
