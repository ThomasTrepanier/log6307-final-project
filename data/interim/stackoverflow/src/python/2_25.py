def sumOfUnique(nums):
    counts = {}
    for i in nums:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1

    uniques = [k for k, v in counts.items() if v == 1]
    print(uniques)
    return sum(uniques)  # return the sum of the list elements

print(sumOfUnique([1, 2, 1, 3, 4, 1]))
