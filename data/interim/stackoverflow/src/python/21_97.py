def check_arr_str(li):

    #Check if any instance of the list is not a string
    flag = any(not isinstance(i,str) for i in li)

    #If any instance of an item  in the list not being a list, or the input itself not being a list is found, throw exception
    if (flag or not isinstance(li, list)):
        raise TypeError('I am expecting list of strings')
