def contains(list1,list2):

    str1=""
    for i in list1:
        str1+=str(i)

    str2=""
    for j in list2:
        str2+=str(j)

    if str1 in str2:
        return True

    else:
        return False
