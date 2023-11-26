def my_func(st):

    res = []
    #Iterate over the character
    for index in range(len(st)):
        if index % 2 == 0:
            #Refer to each character via index and append modified character to list
            res.append(st[index].upper())
        else:
            res.append(st[index].lower())

    #Join the list into a string and return
    return ''.join(res)
