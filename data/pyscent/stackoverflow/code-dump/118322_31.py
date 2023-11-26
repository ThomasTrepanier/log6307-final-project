from collections import Counter

def perm_palindrome(string_input):

    count_dict = Counter(string_input)
    odd_count = 0

    for values in count_dict.values():
        if values % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    else:
        return True


string_value = "aabb"
output = perm_palindrome(string_input=string_value)
print("Answer of permutation palindrome if {} is :::: {}".format(string_value, output))
