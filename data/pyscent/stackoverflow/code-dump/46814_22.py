def up_arrow(a, b):
  if b <= 2:
    if b < 0:
      raise ValueError
    return (1, 2, 4)[b]
  elif a == 1:
    if b >> 363:
      raise ValueError
    return 1 << b  # This may run out of memory for large b.
  elif a == 2:
    if b > 5:
      raise ValueError
    if b == 5:
      return 1 << 65536
    return (16, 65536)[b - 3]
  elif a == 3:
    if b > 3:
      raise ValueError
    return 65536
  else:
    raise ValueError
