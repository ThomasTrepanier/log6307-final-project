import bisect

def find_next(x, a):
  i = bisect.bisect_right(x, a)
  if i:
    return x[i]
  return None

def is_sequence(x):
  ans = True
  for i in x[:-1]:
    next_num = find_next(x, i)
    if next_num and i+1 != next_num:
      ans = False
      break
  return ans

print(is_sequence([1,2,3,4])) # True
