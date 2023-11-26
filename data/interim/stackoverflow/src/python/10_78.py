class MyData(dict):

    def __hash__(self):
        return hash((k, repr(v)) for k, v in self.items())

l = [
    {1: {'a': [1, 2, 3], 'b': 4}},
    {2: {'a': [4, 5, 6], 'd': 5}},
    {3: {'b': 4, 'a': [1, 2, 3]}},
    {4: {'a': (4, 5, 6), 'd': 5}},
]

s = set([MyData(*d.values()) for d in l])
