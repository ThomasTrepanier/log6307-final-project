def check_arr_str(li):

    #Filter out elements which are of type string
    res = list(filter(lambda x: isinstance(x,str), li))

    #If length of original and filtered list match, all elements are strings, otherwise not
    return (len(res) == len(li) and isinstance(li, list))

