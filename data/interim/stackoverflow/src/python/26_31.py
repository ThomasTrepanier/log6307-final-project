def make_bricks(small, big, goal):
  
  if (big is not 0 and (big*5+small*1 > goal) and goal % 5 <= small) or goal < small or big*5+small*1 == goal:
    return True
  else:
    return False
