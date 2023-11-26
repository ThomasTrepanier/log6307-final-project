def odd(n):
    nums = []
    for i in range(1, n*2+1):
        if i%2==0:
            pass
        else:
            nums.append(i)
    return nums
odd(10)
