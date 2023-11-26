def required_steps (n = 0, r = 1):
  if n == 0:
    return r - 1
  else:
    return required_steps(n - 1, r * 2)

for x in range(6):
  print(f"f({x}) = {required_steps(x)}")

# f(0) = 0
# f(1) = 1
# f(2) = 3
# f(3) = 7
# f(4) = 15
# f(5) = 31
