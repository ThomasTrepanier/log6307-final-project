def make_bricks(small, big, goal):
  total_bricks = (1 * small) + (5 * big)
  if total_bricks >= goal:
    if goal%5 == 0:
      if goal/5 <= goal:
        x = True
    elif goal%5 <= small:
        x = True
    else:
      x = False
  else:
    x = False
  return x
