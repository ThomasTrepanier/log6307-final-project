class Solution:
    def twoSum(self, nums, target):
        for i, a in enumerate(nums, start=0):
            for j, b in enumerate(nums[i+1:], start=0):
                if a+b==target:
                    return [i, j+i+1]

test_case = Solution()
array = [3, 2, 4]
print(test_case.twoSum(array, 6))

array = [1, 5, 7]
print(test_case.twoSum(array, 6))

array = [2, 7, 11, 15]
print(test_case.twoSum(array, 9))
