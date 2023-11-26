from collections import Counter

class Solution:
    
    def sumOfUnique(self, nums):
        counts = Counter(nums)
        unique_list = [x for x in counts if counts[x] == 1]
        return sum(unique_list)


