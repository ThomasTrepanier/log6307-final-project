import random

def myfunc2(old):
  new = ''
  for c in old:
    lower = random.randint(0, 1)
    if lower:
      new += c.lower()
    else:
      new += c.upper()
  return new
