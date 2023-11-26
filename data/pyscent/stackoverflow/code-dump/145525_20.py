def spy_game(nums):
    a=[]
    for i in nums:
        if i == 0:
            a.append(i)
        if i == 7:
            a.append(i)
    if a ==  [0,0,7]:
        return True
    else:
        return False
