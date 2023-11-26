N = 10 # size of a "word"
# constraints on the amounts of type of characters in a word
lower_bound1, lower_bound2 = 3, 3

def word_partitioner(list1, min1, list2, min2, word_length=10):
    # return pairs which entries represent the amount of characters to be used to form a word of length word_length
    # min1, min2 represents the lower bounds of the type of characters to be contained in the word
    return [(i, j) for i, j in product(range(min1, len(list1)), range(min2, len(list2))) if i + j == word_length]

partitions = word_partitioner(list1, lower_bound1, list2, lower_bound2, N)
print(partitions)
