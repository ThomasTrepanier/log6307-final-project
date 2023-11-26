def stop_at_four(lst):
    n = 0
    new_lst = []
    while lst[n] != 4:
        new_lst.append(lst[n])
        n += 1
    return new_lst
lst = [1,2,4,6,12]
print(stop_at_four(lst))
