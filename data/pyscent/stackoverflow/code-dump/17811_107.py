def matchs_path(_pattern, _input):
  _a, _b = filter(None, _pattern.split('/')), filter(None, _input.split('/'))
  while True:
    _val, _val2 = next(_a, None), next(_b, None)
    if _val is None and _val2 is None:
      return True
    if _val != '*' and _val != _val2:
      return False
    if _val == "*":
      _to_see = next(_a, None)
      if _to_see is None:
        return True
      while True:
        c = next(_b, None)
        if c is None:
          return True
        if c == _to_see:
          break
