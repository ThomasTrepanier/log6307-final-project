def squares(n):
       L = []
       for num in range(1,n+1):
           val = num*num 
           L.append(val)
       return L
print(squares(16))
