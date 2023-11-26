# A Python program to print all
# permutations of given length
from itertools import permutations

# check_validity(tuple1) checks whether the combination contains at least 3 elements from list a and at least 3 elements from list b
def check_validity(tuple1):
    a_cnt = 0
    b_cnt = 0
    for t in tuple1:
        if t in a:
            a_cnt += 1
        if t in b:
            b_cnt += 1
    if a_cnt >= 3 and b_cnt>=3:
        return True
    else:
        return False

# Get all permutations of length 10
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list1 = a + b     # merge two lists
perm = list(permutations(list1, 10))     # find all permutaions

# Print the obtained permutations
result_perm = []
for tuple1 in perm:          # list of permutations contain tuples
    if check_validity(tuple1) == True:    # check_validity(tuple1) checks whether the combination contains at least 3 elements from list a and at least 3 elements from list b
        result_perm.append("".join(list(map(str,tuple1))))     # join characters from tuple to generate a string

result_perm
