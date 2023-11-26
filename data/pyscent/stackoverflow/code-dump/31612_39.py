def print_keys(dic):
    for key, value in dic.items():
        print(key)
        if isinstance(value, dict):
            print_keys(value)
