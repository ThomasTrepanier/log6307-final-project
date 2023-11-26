def counter(my_list):
    my_list = sorted(my_list)
    first_val, *all_val = my_list
    p_index = my_list.index(first_val)
    my_counter = {}
    for item in all_val:
         c_index = my_list.index(item)
         diff = abs(c_index-p_index)
         p_index = c_index
         my_counter[first_val] = diff 
         first_val = item
    c_index = my_list.index(item)
    diff = len(my_list) - c_index
    my_counter[first_val] = diff 
    return my_counter

def my_func(data):
    if not data or not isinstance(data, list):
        return
    # get the first value
    first_val, *all_val = data
    if not isinstance(first_val, list):
        return
    # count items in first value
    p = counter(first_val) # counter({1: 2, 3: 1, 5: 1, 7: 1})
    # collect all common items and calculate the minimum occurance in intersection
    for val in all_val:
        # collecting common items
        c = counter(val)
        # calculate the minimum occurance in intersection
        inner_dict = {}
        for inner_val in set(c).intersection(set(p)):
            inner_dict[inner_val] = min(p[inner_val], c[inner_val])
        p = inner_dict
    # >>>p
    # {1: 2, 7: 1}
    # Sort by keys of counter
    sorted_items = sorted(p.items(), key=lambda x:x[0]) # [(1, 2), (7, 1)]
    result=[i[0] for i in sorted_items for _ in range(i[1])] # [1, 1, 7]
    return result
