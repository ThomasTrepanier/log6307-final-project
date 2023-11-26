def combine_lists(list1, list2):
    for n in range(1, len(list1)+1):
        list2.append(list1[-n])
    return list2

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))
