class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)
