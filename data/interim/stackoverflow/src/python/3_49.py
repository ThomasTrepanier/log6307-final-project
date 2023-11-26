def name_counts(name_list):
    result_dict = {}
    for name in name_list:
        names = name.split(" ")
        if names[0] in result_dict:
            result_dict[names[0]] += 1
        else:
            result_dict[names[0]] = 1
    return result_dict 
