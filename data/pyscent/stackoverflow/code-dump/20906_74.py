from functools import reduce
arr = [17, 2, 3, 6, 1, 3, 1, 9, 5, 3]
def func(acc,x):
    if not acc:
        return [x]
    if acc[-1]<x:
        return acc+[x]
    else:
        return acc[:-1]+[x]+acc[-1:]

def my_sort(x):
    moresorted = reduce(func,x,[])
    print(moresorted)
    if x==moresorted:
        return moresorted
    else:
        return my_sort(moresorted)

print('arr:',arr)
arr_sorted = my_sort(arr)
print('arr sorted:',arr_sorted)
