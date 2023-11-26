def ListCheck():
    number = 11
    nums = [10, 15, 3, 7, 9, 6, 4, 8]
    found = 0
    while found == 0:
        if len(nums) < 2: # check if array has at least 2 numbers
            break
        while len(nums) > 1:
            comparenum = nums.pop() # removes comparable number from array to avoid false true if nums has item == number*2 
            if (number - comparenum) in nums:
                print(True)
                found = 1
                break

    if found == 0:
        print(False)
        

ListCheck()
exit
