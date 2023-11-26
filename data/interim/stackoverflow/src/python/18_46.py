example_input = {'key0a': "test", 'key0b': 
                 {'key1a': {'key2a': 'end', 'key2b': "test"} ,'key1b': "test"}, 
                 "something": "else"}
def parse(d):
  x = SimpleNamespace()
  _ = [setattr(x, k, parse(v)) if isinstance(v, dict) else setattr(x, k, v) for k, v in d.items() ]    
  return x

result = parse(example_input)
print (result)
