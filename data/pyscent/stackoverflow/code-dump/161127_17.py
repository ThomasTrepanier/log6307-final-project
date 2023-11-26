def arrange_list(arr):
    value = 0
    for x in range(len(arr)-1):
        if arr[x] != 0:
            value += arr[x]
        else:
            value = 0
        if arr[x+1] != 0:
            arr[x] = 0
        else:
            arr[x] = value
            value = 0
    if value !=0:
        arr[-1] = value + arr[-1]
    return arr
