my_dict = {1: "name",
           2: "last_name",
           3: "name",
           4: "last_name",
           5: "name",
           6: "last_name"}

def my_function(my_dict):

    new_dict = {v:[k for k in my_dict.keys() if my_dict[k] == v] for v in my_dict.values()}

    return new_dict

print(my_function(my_dict))
