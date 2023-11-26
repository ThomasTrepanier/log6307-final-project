def spy_game(nums):
    for index, n in enumerate(nums):
        if n==0:
            for index1,n1 in enumerate(nums[index+1::]):
                if n1 == 0:
                    for index2,n2 in enumerate(nums[index1+1::]):
                        if n2 == 7:
                            return True
                        
                    else:
                        return False
