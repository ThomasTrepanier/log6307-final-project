def ack(m, n):
  if n < 0:
    raise ValueError
  if m in (0, 1):
    return n + (m + 1)  # This may run out of memory for large n.
  elif m == 2:
    return (n << 1) + 3  # This may run out of memory for large n.
  elif m == 3:
    if n >> 360:
      raise ValueError
    return (1 << (n + 3)) - 3  # This may run out of memory for large n.
  elif m == 4:
    if n > 2:
      raise ValueError
    if n == 2:
      return (1 << 65536) - 3
    return (13, 65533)[n]
  elif m == 5:
    if n > 0:
      raise ValueError
    return 65533
  else:
    raise ValueError

print([ack(m, 0) for m in range(6)])
print([ack(m, 1) for m in range(5)])
print([ack(m, 2) for m in range(5)])
print([ack(m, 3) for m in range(4)])
print([ack(m, 4) for m in range(4)])
