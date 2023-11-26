def sum_divisors(n):
  sum = 0
  accum = 1
  while n != 0 and accum < n:
    if n % accum == 0:
      sum += accum
    accum += 1
  return sum



print(sum_divisors(6)) # prints 6
print(sum_divisors(12)) # prints 16
