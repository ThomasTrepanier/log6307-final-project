def set_impl(l):
  bag = set()
  res = []
  for i in l:
    if i in bag:
      res.append(i)
      bag.remove(i)
    else:
      bag.add(i)
