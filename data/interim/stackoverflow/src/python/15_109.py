def summer_69(arr):
    a = 0
    for nums in arr: 
        if nums == 6:
            for items in arr[arr.index(6):]:
                a = a+ items
                if items == 9:
                    break
    return sum(arr)-a
