def strip2single(textarr):
    if len(textarr)==0:
        return ""
    result=textarr[0]
    for i in range(1,len(textarr)):
        if textarr[i]!=textarr[i-1]:
            result=result+' '+textarr[i]
    return(result)


mystring = "my friend's new new new new and old old cats are running running in the street"

y=strip2single(mystring.split())
print(y)
