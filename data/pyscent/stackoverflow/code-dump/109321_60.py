def myfunc(str):
    rstr = ''
    for i in range(len(str) ):
        if i % 2 == 0 :
            # str[i].upper()
            rstr = rstr + str[i].upper()
        else:  
            #str[i].lower()
            rstr = rstr + str[i].lower()
    return rstr        
