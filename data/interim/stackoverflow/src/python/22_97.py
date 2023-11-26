from collections import Counter

def permutationPalindrome(string):
    counterObject = Counter(char for char in string.lower() if char.isalpha())
    no_of_odd = 0
    for value in counterObject.values():
        if value % 2 != 0:
            no_of_odd += 1
        if(no_of_odd > 1):
            return False
    return True
