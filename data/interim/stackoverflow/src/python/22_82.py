def repeatedString(s, n):
    if len(s)==1 and s=="a":
        return n
    count=s.count("a") 
    x,y=divmod(n,len(s))
    count=count*x
    str=s[:y]
    return count+str.count("a")
