def summer_69(arr):
    y = []
    for x in arr:
        if 6 in arr:
            a = arr.index(6)
            b = arr.index(9)
            del arr[a:b+1]
            y = arr
        elif arr == []:
            return "0"
        else:
            return sum(arr)
    return sum(y)
print(summer_69([]))                                                          #0
print(summer_69([1, 3, 5]))                                                   #9
print(summer_69([4, 5, 6, 7, 8, 9]))                                          #9
print(summer_69([2, 1, 6, 9, 11]))                                            #14
print(summer_69([2, 1, 6, 9, 6, 11, 25, 36, 11, 9, 4, 6, 4, 6, 3, 9, 15]))    #22
