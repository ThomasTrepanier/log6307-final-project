def searchInsert(self, nums, target):
    try:
        return nums.index(target)
    except IndexError:  # best to use explicit except
        for index, value in enumerate(nums):  # more pythonic than range(len(nums))
             if value > target:
                  return index
        return len(nums)
