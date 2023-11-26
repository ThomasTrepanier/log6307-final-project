def repeatedString(s, n):
    if len(s)==1 and s=='a':
        return n
    cnt_a=0
    for i in s:
        if i == 'a':
            cnt_a+=1
    if cnt_a % 2 == 0:
        no_a = (cnt_a/len(s)) * n
        return math.ceil(no_a)
    else:
        no_a = (cnt_a/len(s)) * n
        return math.floor(no_a)
