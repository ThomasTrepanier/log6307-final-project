def func(my_dict):
    new_dict = {}
    new_dict['name'] = {}
    new_dict['last_name'] = {}
    for i in my_dict.keys():
        if i%2 == 1 :
            new_dict['name'].append(i)
        else :
            new_dict['last_name'].append(i)
    return new_dict
