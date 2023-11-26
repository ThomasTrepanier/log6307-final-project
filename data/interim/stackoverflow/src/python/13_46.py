def pick(lst, ref, res=None):
  if res == None: res = []
  if len(lst) == 0: return res
  if ref[0] >= lst[0]:
    res.append(ref[0])
    lst.pop(0)
  elif len(ref) == 1 and ref[0] < lst[0]:
    # res.extend(lst) # if want to append the rest of lst instead of stop the loop
    # or do whathever is best for you
    return res
  else: ref.pop(0)
  pick(lst, ref, res)
  return res


list_b = [0.6, 1.7, 3, 3.9]
list_bb = [0.5]
list_a = [0.6, 0.9, 1.2, 1.5, 2, 2.5, 3, 4, 4.5]

print(pick(list_a, list_b))
#=> [0.6, 1.7, 1.7, 1.7, 3, 3, 3]

print(pick(list_a, list_bb))
#=> []
