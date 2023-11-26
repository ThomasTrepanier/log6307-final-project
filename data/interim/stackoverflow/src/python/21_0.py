def solution(s): # 's' should be a binary input (011100)
    while s[0] == "0":
        s = s[1:]
    ones = s.count('1')
    zeros = s.count('0')
    return ones*2+zeros-1
