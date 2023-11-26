def number_69(arr):
    sum = 0
    stop = False
    for num in arr:
        if num == 6:
            stop = True
        elif num == 9:
            stop = False
        elif stop is False:
            sum = sum + num
    return sum

print(number_69([2, 1, 6, 9, 11]))
