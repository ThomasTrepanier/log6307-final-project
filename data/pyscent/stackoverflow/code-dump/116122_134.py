def maxs(iterable):
    max = None
    count = 0
    for index, value in enumerate(iterable):
        if index == 0 or value >= max:
            if value != max:
                count = 0
            max = value
            count += 1
    return count * [max]


print (maxs([5, 6, 7, 8, 8]))   # [8, 8]
print (maxs([3, 2, 4, 5, 1, 2, 4, 5, 2, 5, 0])) # [5, 5, 5]
print (maxs([])) # []
