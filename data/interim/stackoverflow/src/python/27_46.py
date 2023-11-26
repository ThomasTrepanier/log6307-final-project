def checkString(inp):
    # print(list(inp))
    return state1(list(inp))

testcases = ["abb","a","ab","abba", "","abbabbb","abbabbaaabbaaabbabb"]
for i in testcases:
    print(checkString(i))
