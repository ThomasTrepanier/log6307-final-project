def is_power_of_two(n):

 #Check Number for Zero
  if n==0:
    return False
  else:
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
      n = n / 2 
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
      return True
    return False
