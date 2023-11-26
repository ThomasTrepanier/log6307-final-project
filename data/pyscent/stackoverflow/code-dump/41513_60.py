def find(key, value):
  if isinstance(value, dict):
    for k, v in value.iteritems():
      if k == key:
        yield v
      else:
        for result in find(key, v):
          yield result
  elif isinstance(value, list):
    for element in value:
      for result in find(key, element):
        yield result
