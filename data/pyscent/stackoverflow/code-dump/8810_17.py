d = {'Name1': {'NNum': '11', 'Node1': {'SubNodeA': 'Thomas', 'SubNodeB': '27'}, 'Node2': {'SubNodeA': 'ZZZ', 'SubNodeD': 'XXX', 'SubNodeE': 'yy'}, 'Node3': {'child1': 11, 'child2': {'grandchild': {'greatgrandchild1': 'Rita', 'greatgrandchild2': 'US'}}}}}
def keys(d, c = []):
  return [i for a, b in d.items() for i in ([c+[a]] if not isinstance(b, dict) else keys(b, c+[a]))]

result = list(map('.'.join, keys(d)))
