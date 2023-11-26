def required_steps (n = 0, r = 1):
  if n == 0:
    return r - 1
  else:
    return required_steps(n - 1, r << 1)
