c = {}

def ack(m, n):
  global c

  if m == 0: return n + 1
  else:
    if "{}-{}".format(m, n) in c: return c["{}-{}".format(m, n)]
    else: ret = ack(m - 1, 1) if n == 0 else ack(m - 1, ack(m, n - 1))

    c["{}-{}".format(m, n)] = ret
    return ret
