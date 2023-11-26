data = [(1,2,3), (4,5,6), (7,8,9)]
def combos(d, c = []):
   if len(c) == len(d):
     yield c
   else:
     for i in d:
        if i not in c:
           yield from combos(d, c+[i])

def product(d, c = []):
  if c:
    yield tuple(c)
  if d:
    for i in d[0]:
      yield from product(d[1:], c+[i])

result = sorted({i for b in combos(data) for i in product(b)})
final_result = [a for i, a in enumerate(result) if all(len(c) != len(a) or len(set(c)&set(a)) != len(a) for c in result[:i])]
