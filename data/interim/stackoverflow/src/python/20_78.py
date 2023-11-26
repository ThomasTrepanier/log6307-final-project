def summer_69(arr):
    toSum = True
    sum = 0
    for x in arr:
        if toSum :
            if(x == 6):
                toSum = False
            else :
                sum += x
        else :
            if(x == 9):
                toSum = True
    return sum
