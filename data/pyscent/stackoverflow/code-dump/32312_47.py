def myprint(word, n, delim):
    ans = [word] * n 
    return delim.join(ans)
    
print(myprint('cat',3,'petting'))
