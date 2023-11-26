def find_sum(s, lst):
    s.sort()
    good_pairs = []
    indices = {x: i for i, x in enumerate(lst[:len(lst)//2])}
    # print(indices)
    for i, x in enumerate(lst):
        target = s - x
        if target in indices:
            good_pairs.append((lst[i], lst[indices[target]]))

    return good_pairs

lst = [2, 4, 5, 6, 7, 8]
print(find_sum(12, lst)) 
