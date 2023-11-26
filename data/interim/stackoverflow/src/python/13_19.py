def middlesplit(s,delim=" "):
    if delim not in s:
        return (s,)
    midpoint=(len(s)+1)//2
    left=s[:midpoint].rfind(delim)
    right=s[:midpoint-1:-1].rfind(delim)    
    if right>left:
        return (s[:-right-1],s[-right:])
    else:
        return (s[:left],s[left+1:])
