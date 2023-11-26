def most_frequent_letter(word):
    letters = list(word)
    return (max(set(letters), key = letters.count))

print(most_frequent_letter('mmmaaa'))
# output:m
print(most_frequent_letter('some apples are green'))
# output: e
