from string import ascii_letters
from collections import Counter
s = "Mr. owl ate my Metal worm"

def is_permutation_palindrome(s):
 return len([i for i in Counter(c.lower() for c in s if c in ascii_letters).values() if i&1]) < 2

print(is_permutation_palindrome(s))
