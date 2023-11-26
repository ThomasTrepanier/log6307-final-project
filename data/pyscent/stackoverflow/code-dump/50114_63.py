def count_substring(string, sub_string):
    n = len(sub_string)
    ans = 0
    for i in range(0,len(string)):
        if(i+n > len(string)):#out of range problem
            break
        ans+=string.count(sub_string,i,i+n)
    return ans
