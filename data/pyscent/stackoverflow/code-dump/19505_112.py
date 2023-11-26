class Solution:
    def twoSum(self, nums, target):
        look_for = {}
        for n,x in enumerate(nums):
            try:
                return look_for[x], n
            except KeyError:
                look_for.setdefault(target - x,n)

test_case = Solution()
array = [1, 5, 7]
array2 = [3,2,4]
given_nums=[2,7,11,15]
print(test_case.twoSum(array, 6))
print(test_case.twoSum(array2, 6))
print(test_case.twoSum(given_nums,9))
