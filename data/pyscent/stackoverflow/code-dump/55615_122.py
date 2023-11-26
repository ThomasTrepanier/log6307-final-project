def summer_69(lst):
  """Return the sum of the numbers in the array, 
     except ignore sections of numbers starting with a 6 and extending to the next 9 
     (every 6 will be followed by at least one 9). Return 0 for no numbers
  """
  if not lst:
    return 0
  else:
    _sum = 0
    active = True
    for x in lst:
      if active: 
        if x != 6:
          _sum += x
        else:
          active = False
      else:
        if x == 9:
          active = True
    return _sum

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
