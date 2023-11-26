def chkList(lst):
    return True if lst in list_of_lists else False

list_of_lists = [[2,2,2,3],[2,3,4],[2,2,6]]
print(chkList([2,2,6]))
