from collections import OrderedDict, defaultdict

class DefaultOrderedDict(OrderedDict):
    def __missing__(self, k):
        self[k] = set()
        return self[k]

d = DefaultOrderedDict()  # Python 3.7+: d = defaultdict(set)

for i in lst:
    d[(i['number'], i['favorite'])].add(i['color'])

res = [{'number': num, 'favorite': fav, 'color': col} for (num, fav), col in d.items()]

print(res)
# [{'color': {'green', 'red'}, 'favorite': False, 'number': 1},
#  {'color': {'red'}, 'favorite': True, 'number': 1},
#  {'color': {'red'}, 'favorite': False, 'number': 2}]
