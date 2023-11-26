def encode(code):
    cpt=1 
    n=len(code)
    res=''
    for i in range(n):
        if i == n-1 or code[i] != code[i+1]:
            res += str(cpt)+code[i]
            cpt=1
        else: cpt+=1
    return res
