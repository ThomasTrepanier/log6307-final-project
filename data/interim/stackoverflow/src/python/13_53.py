import math

def fibonacci_numbers():
  how_many_numbers = int(input("\nHow many Fibbonacci numbers you want print: "))
  i = 0
  res = [0, 1]
  for i in range(how_many_numbers):
      res.append(sum(res[-2:]))
  digits = int(math.log10(res[i]))+1
  ind_digits = int(math.log10(how_many_numbers-1))+2
  for i in range(how_many_numbers):
      print("{:<{ind_digits}} {:>{digits}}".format("{}.".format(i + 1), res[i], ind_digits=ind_digits, digits=digits))


fibonacci_numbers()
