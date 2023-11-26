class Solution:
    def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            ls=[]
            l2=[]
            for i in nums:
                ls.append(target-i)

            for i in range(len(ls)):
                if ls[i] in nums  :
                    if i!= nums.index(ls[i]):
                        l2.append([i,nums.index(ls[i])])            
            return l2[0]


x= Solution()
x.twoSum([-1,-2,-3,-4,-5],-8)
