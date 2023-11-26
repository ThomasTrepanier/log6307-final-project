def test(string):
    s = string.split()
    if any(word in Group_A for word in s) and any(word in Group_B for word in s):
        return 1
    else:
        return 0
