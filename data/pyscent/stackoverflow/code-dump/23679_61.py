def replace_nth(list_of_lists, n, value):
    for sublist in list_of_lists:
        for i, v in enumerate(sublist):
            if not i % n:
                sublist[i] = value

a = [[1,2,3,4,5,6],
     [7,8,9,10,11,12],
     [13,14,15,16,17,18]]

replace_nth(a, 3, 0)
print(a)  # -> [[0, 2, 3, 0, 5, 6], [0, 8, 9, 0, 11, 12], [0, 14, 15, 0, 17, 18]]
