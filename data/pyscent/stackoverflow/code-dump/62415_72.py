def summer_69(arr):
    skate = arr
    guitar = []
    for i in range(len(arr)):
        if 6 in arr:
            guitar = skate[skate.index(6):skate.index(9)+1]
            return abs(sum(skate) - sum(guitar))
        else:
            return sum(skate)
