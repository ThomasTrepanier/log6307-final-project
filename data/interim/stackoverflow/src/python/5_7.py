def swap(num):
  num = str(float(num))
  a, b = num.split('.')
  res = b + '.' + a
  return res


print(swap(2)) # 0.2
print(swap(21.34)) # 34.21
