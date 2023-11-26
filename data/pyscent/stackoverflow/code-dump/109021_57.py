def myfunc(a):
    newString = ''
    for count, ele in enumerate(a, 0):
        if count %2 == 0:
            newString += (a[count].lower())
        else:
            newString += ((a[count].upper()))
    return newString
