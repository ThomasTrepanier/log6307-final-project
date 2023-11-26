list_ = [('Books', '10.000'),('Pen', '10'),('test', 'a')]

def fix_list(list_):
    def check_and_convert(val_1, val_2):
        try:
            return val_1, float(val_2)
        except:
            return val_1, val_2

    ret_list = []
    for val_1, val_2 in list_:
        ret_list.append(check_and_convert(val_1, val_2))
    return ret_list


print(fix_list(list_))
# >>> [('Books', 10.0), ('Pen', 10.0), ('test', 'a')]
