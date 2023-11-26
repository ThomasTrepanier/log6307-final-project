def sortedList(li, start=0, end=None):
        if end is None:
                end = len(li)
        fi = []
        fi[:start] = li[:start]
        fi[start:end] = sorted(li[start:end])
        return fi


li = [2, 1, 4, 3, 0]
print(li)
print(sortedList(li, 1))
