def name_lists(n_list):
    result_dict = {}
    n_list.sort()
    for name in n_list:
        names = name.split(" ")
        if names[0] in result_dict:
            result_dict[names[0]].append(name)
        else:
            result_dict[names[0]] = [name]
    return result_dict
