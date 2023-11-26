def list_sum(lst1, lst2):
    out = []
    for i, lst in enumerate([lst1, lst2]):
        if len(lst) > 0:
            out.append(int(''.join(str(x) for x in lst)))
        else:
            if i == 0:
                return lst2
            else:
                return lst1
    return [int(x) for x in str(out[0]+out[1])]

list_sum([6,9,8],[5,9,2])
