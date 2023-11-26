class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)         
        nums.sort()                 
        for i,j in enumerate(nums): 
            if target == j:         
                return i            
