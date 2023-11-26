def expanding(L):
    
    x=list()
    for i in range(len(L)-2):
        if abs(L[i+1]-L[i+2]) > abs(L[i]-L[i+1]):
            x.append(True)
        else:
            x.append(False)
    return all(x)
print(expanding([1,3,7,2,9]))
