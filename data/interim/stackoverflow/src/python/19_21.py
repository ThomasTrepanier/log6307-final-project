def romanToDecimal(self, S): 
    d = {
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
    }
    res = 0
    old = 'I'
    
    for i in S[::-1]:
        if d[i] >= d[old]:
            res = res + d[i]
        else:
            res = res - d[i]
        old = i
        
    return res
