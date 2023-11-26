lst = [[1, 2, 3, 4],
        [5, 6],
        [7,8,9,10]]

def get_item(lst,i):
    current = 0
    for sublist in lst:
        index = i - current
        if 0 <= index < len(sublist):
            return sublist[index]
        current += len(sublist)
    raise Exception("index out of range {}".format(i))

print(get_item(lst,0),get_item(lst,6),get_item(lst,9))
