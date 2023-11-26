def summer_69(series):
  in_summer = False
  cur_sum = 0
  for v in series:
    if in_summer:
      if v == 9:
        in_summer = False
    else:
      if v == 6:
        in_summer = True
      else:
        cur_sum += v
  return cur_sum
