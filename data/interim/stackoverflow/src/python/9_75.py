def find_two_sum(lst, n):
    indices = {}
    for idx, num in enumerate(lst):
        indices.setdefault(num, []).append(idx)
    for k, v in indices.items():
        i = v.pop()
        if n - k in indices and indices[n-k]:
            return i, indices[n-k].pop()

print( find_two_sum([3, 1, 5, 7, 5, 9], 6) )
print( find_two_sum([3, 1, 5, 7, 5, 9], 10) )
print( find_two_sum([1, 2, 1, 8], 10) )
print( find_two_sum([5, 5], 10) )
print( find_two_sum([11], 10) )
