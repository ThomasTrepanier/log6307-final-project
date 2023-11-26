def solve(s):
    res=""
    for i in range(len(s)):
        if i==0:
           if s[i].isalpha():
               res+=s[i].capitalize()
           else:
               res+=s[i]
        else:
            if s[i].isalpha() and s[i-1]==' ':
                res+=s[i].capitalize()
            else:
                res+=s[i]
    return res 
