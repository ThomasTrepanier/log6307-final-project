def minSubStr(str1, str2):
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string to check if the characters exist in the first string: ")
    if all(s in str1 for s in str2):
        return True
    return False
