def sum_divisors(n):
  sum = 0
  x = 1
  while n != 0 and x < n :
      
    if n % x == 0  :
      sum += x
    else:
      sum += 0
    x += 1    
  return sum
