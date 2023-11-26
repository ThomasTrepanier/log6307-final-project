def summer_69(arr):
        x = arr.count(6)
        y = arr.count(9)
        # to decide number of iteration required for loop
        z = min(x,y)
        k = 0
        while k < (z) :
            m = arr.index(6)
            n = arr.index(9)
            del arr[m:(n+1)]
            k = k + 1
        print(arr)
        return sum(arr)
