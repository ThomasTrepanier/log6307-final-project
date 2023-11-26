def check_arr_str(li):

    res = list(filter(lambda x: isinstance(x,str), li))
    if (len(res) == len(li) and isinstance(li, list)):
        raise TypeError('I am expecting list of strings')
