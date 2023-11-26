def squares(n):
   L = list(range(n+1))
   L = [num**2 for num in L if num]
   return L
print(squares(16))
