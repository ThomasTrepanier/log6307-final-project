def print_dictionary(dic, indent=0):
    if len(dic) == 0:
        print('\t' * indent + '{}')
    for key, value in dic.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            print_dictionary(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(type(value)))
