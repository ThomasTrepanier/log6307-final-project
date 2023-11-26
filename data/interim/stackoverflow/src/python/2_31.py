def minSubStr(str1, str2):
    if str2 in str1: 
        print(True)
    else:
        print(False)
str1 = input("Enter the first string: ")
str2 = input("Enter the second string to check if the characters exist in the first string: ")
minSubStr(str1, str2)
