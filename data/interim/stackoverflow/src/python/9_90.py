from itertools import groupby
data = {'actor1': {'salary': {'year1': 60, 'year2': 65}, 'age': 30}, 'actor2': {'salary': {'year1': 20, 'year2': 30}, 'age': 17}, 'actor3': {'salary': {'year1': 50, 'year2': 80}, 'age': 25}}
def ave(d):
  _data = sorted([i for b in d for i in b.items()], key=lambda x:x[0])
  _d = [(a, [j for _, j in b]) for a, b in groupby(_data, key=lambda x:x[0])]
  return {a:ave(b) if isinstance(b[0], dict) else round(sum(b)/float(len(b)), 1) for a, b in _d}

result = {'average':ave(list(data.values()))}
