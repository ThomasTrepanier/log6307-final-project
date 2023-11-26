def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

lst = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]

ret =[]
for mini_list in lst:
    ret.append(split_list(mini_list, len(mini_list)))
