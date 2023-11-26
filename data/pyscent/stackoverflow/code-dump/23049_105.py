import re
from itertools import accumulate

def find_index(string, n):
    words = string.split()
    len_word = len(words[n])
    end_index = list(accumulate(map(len, re.split('(\s)' , string))))[::2][n]
    return end_index - len_word, end_index - 1
