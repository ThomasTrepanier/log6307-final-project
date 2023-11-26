from collections import deque

def rotate_values(my_dict):
    # no need to cast the keys to list
    values_deque = deque(my_dict.values())
    values_deque.rotate(1)
    return dict(zip(my_dict.keys(), values_deque))
