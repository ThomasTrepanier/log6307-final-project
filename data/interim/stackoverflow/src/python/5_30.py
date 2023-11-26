array_of_dicts = [{"a": 1, "b": 2}, {"a": 1, "b": "zz", "c": "cc"}, {"a": 1, "b": "2"}]

def get_same_vals(dicts):
  keys = []
  for key in dicts[0].keys():
    is_same = True
    for each_dict in array_of_dicts:
      if not key in each_dict or  each_dict[key] != dicts[0][key]:
        is_same = False
    if is_same:
      keys.append(key)
  return keys

print(get_same_vals(array_of_dicts))  
