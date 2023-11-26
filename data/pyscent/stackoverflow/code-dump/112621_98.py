def foo(my_str_list):
    is_list = isinstance(my_str_list, list) 
    are_strings = all(isinstance(x, str) for x in my_str_list)
    if not is_list or not are_strings:
        raise TypeError("Funtion argument should be a list of strings.")
    ...
