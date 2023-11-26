import itertools

class Solution:
    def twoSum(self, nums, target):
        subsets = []
        for L in range(0, len(nums)+1):
            for subset in itertools.combinations(nums, L):
                if len(subset)!=0:
                    subsets.append(subset)
        print(subsets) #returns all the posible combinations as tuples, note not permutations!
        #sums all the tuples
        sums = [sum(tup) for tup in subsets]
        indexes = []
        #Checks sum of all the posible combinations
        if target in sums:
            i = sums.index(target)
            matching_combination = subsets[i] #gets the option
            for number in matching_combination:
                indexes.append(nums.index(number))
            return indexes
        else:
            return None


test_case = Solution()    
array = [1,2,3]
print(test_case.twoSum(array, 4))
