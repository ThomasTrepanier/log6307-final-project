def except_zero(items: list) -> Iterable: 
    # get and sort non zero values
    non_zero = list(sorted([x for x in items if x!=0]))
    j = 0 
    # place them in correct position
    for i in range(len(items)): 
        if (items[i] != 0): 
            items[i] = non_zero[j]  # get next sorted non_zero value for this position
            j += 1 # update index

    return items
