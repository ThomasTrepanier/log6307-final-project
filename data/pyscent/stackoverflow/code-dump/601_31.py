import math

def comb(x):
    st = 0
    total_comb = 0
    if len(x) < 2: #edge case
        return 0
    if len(x) == 2: #edge case
        return 2
    
    seq_s = 0
    for i in range(1, len(x)-1): 
        if  (x[i]<x[i-1] and x[i]<x[i+1]) or (x[i]>x[i-1] and x[i]>x[i+1]):
            continue
        else:
            print(x[seq_s:i+1])
            if i+1-seq_s == 2 and x[i] == x[i-1]: #means we got two same nums like 10, 10
                pass
            else: total_comb+=math.comb(i+1-seq_s,2)
            seq_s=i
            i+=1
            
    print(x[seq_s:])
    if i+1-seq_s == 2 and x[i] == x[i-1]: #means we got two same nums like 10, 10
        pass
    else: total_comb+=math.comb(len(x)-seq_s,2)
    return total_comb
    

x= [1,2,1,3,4,-2]
print(comb(x))
