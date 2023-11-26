def rotate_values(my_dict):
    if not my_dict:
        return {}
    *rest, last = my_dict.values()
    return dict(zip(my_dict, (last, *rest)))
