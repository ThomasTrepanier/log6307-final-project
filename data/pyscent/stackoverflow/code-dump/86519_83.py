def NumberStream(string):
    global j
    l = len(string)
    count = 0
    res = string[0]
    print("Length of the string is ", l)
    for i in range(l):
        count += 1
        cur_count = 1
        print("Looping")
        for j in range(i+1, l):
            if string[i] != string[j]:
                break
            cur_count += 1
            print(string[i], " and ", string[j], " with cur_count = ", cur_count, " and count = ", count)
        if string[i] == string[j-1] and string[j-1] == str(cur_count):
            return "True"
    return "False"


print(NumberStream("6539923335"))
