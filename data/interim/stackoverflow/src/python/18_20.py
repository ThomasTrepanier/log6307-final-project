def _test():
    a = np.bool_(True)
    b = np.bool_(True)
    c = np.bool_(False)
    d = np.bool_(False)
    # test_1
    print(a is True)
    print(a is False)
    print(a == True)
    print(a == False)
    print(c is True)
    print(c is False)
    print(c == True)
    print(c == False)
    # test_2
    print(a is b)
    print(a == b)
    print(a and b)
    print(a or b)
    # test_3
    print(a is c)
    print(a == c)
    print(a and c)
    print(a or c)
    # test_4
    print(c is d)
    print(c == d)
    print(c and d)
    print(c or d)
    # test_5
    print(not a)
    print(not c)
