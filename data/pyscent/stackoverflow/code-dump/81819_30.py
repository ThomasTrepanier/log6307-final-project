from collections import defaultdict
import operator
def NumberStream(string):
    count={}
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            count[str(i)]=string[i]
            count[str(i+1)]=string[i+1]
    print(count)   
    res=defaultdict(int)
    for key, item in count.items():
        res[item]+=1
    print(res)
    stream=0
    for key, item in res.items():
        if int(key)== item:
            stream=key
    
    if int(stream)> 0:
        return "true"
    else: return "false"


    
