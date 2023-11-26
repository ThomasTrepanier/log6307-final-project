def fill_in_numbers(lst):
    i=0
    while True:
        if lst[i+1] != lst[i] + 1:
             lst.insert(i+1, lst[i]+1)
        i+=1
        if lst[-1] - lst[i]== 1:
            break
    return lst
