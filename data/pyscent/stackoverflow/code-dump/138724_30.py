def combine_lists(list1, list2):
    Jamies_list.reverse()
    final_list = Drews_list + Jamies_list
    return final_list
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))
