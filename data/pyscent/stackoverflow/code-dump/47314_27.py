c = {}

def ack(m, n):
  global c

  if m == 0: return n + 1
  else:
    key = "{}-{}".format(m, n)
    if key in c: return c[key]
    else: ret = ack(m - 1, 1) if n == 0 else ack(m - 1, ack(m, n - 1))

    c[key] = ret
    return ret
