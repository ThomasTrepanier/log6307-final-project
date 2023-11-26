def main(n, a=1):
  if n<=1:
    return [a]
  else:
    return [a, *main(n-1, 2*a+1)]

print(main(10))
# [ 1, 3, 7, 15, 31, 63, 127, 511, 1023 ]

print(main(1))
# [1]
