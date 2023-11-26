def yield_non_summer(series):
  in_summer = False
  def stateful_summer_predicate(v):
    nonlocal in_summer
    if in_summer and v == 9:
      in_summer = False
      return True  # 9 is still in summer
    elif not in_summer and v == 6:
      in_summer = True
    return in_summer
  return (v for v in series if not stateful_summer_predicate(v))

def summer_69(series):
  return sum(yield_non_summer(series))
