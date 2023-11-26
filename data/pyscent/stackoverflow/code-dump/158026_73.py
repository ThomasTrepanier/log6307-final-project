import itertools
teams = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
combo = list(itertools.combinations(teams, 2))
def group(c = [], s = []):
   _c = {i for b in c for i in b}
   if all(i in _c for i in teams):
     yield c
     _s = [i for i in combo if i not in s]
     if _s:
       yield from group(c=[_s[0]], s=s+[_s[0]])
   else:
     _c = {i for b in c for i in b}
     _s = [i for i in combo if i not in s and all(j not in _c for j in i)]
     for i in _s:
       yield from group(c=c+[i], s = s+[i])


results, combos = [], group()
_start = next(combos)
while all(all(j not in i for i in results) for j in _start):
   results.append(_start)
   _start = next(combos)
