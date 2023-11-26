def findSubstring(s, k):
    i = 0
    lst = []
    count = 0
    tempL = []
    
    while(i != len(s)):
        a = i+k
        temp = s[i:a]
        lst.append(temp)
        if a != len(s):
            i+=1
        else:
            break
    
    for word in lst:
        count = 0
        for alphabet in word:
            if alphabet in 'aeiou':
                count += 1
        tempL.append(count)
    print(lst)
    print(tempL)
    return 

s = 'azerdii'
k = 5
print(findSubstring(s, k))
