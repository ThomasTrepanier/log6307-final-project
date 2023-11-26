def yield_non_summer(series):
  in_summer = False
  def stateful_summer_predicate(v):
    nonlocal in_summer
    in_summer = (in_summer or v == 6) and v != 9
    return in_summer
  return (v for v in series if not stateful_summer_predicate(v))

def summer_69(series):
  return sum(yield_non_summer(series))
