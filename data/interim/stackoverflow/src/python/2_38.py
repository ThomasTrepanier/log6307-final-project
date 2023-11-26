from functools import reduce
from operator import and_, or_, contains
def containsAll(str1, str2):
    return reduce(and_, map(contains, len(str2)*[str1], str2))
str1 = input("Enter the first string:")
str2 = input("Enter the second string to check if all characters exist:")
containsAll(str1,str2)
