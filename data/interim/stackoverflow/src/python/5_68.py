def beginning(list1):
    sub_list = []
    final_list = []
    if len(list1) > 10:
        sub_list = list1[:10]
        count = 0
    while (count<len(sub_list)) and (sub_list[count] != "bye"):
        final_list.append(sub_list[count])
        count = count + 1
    return final_list
