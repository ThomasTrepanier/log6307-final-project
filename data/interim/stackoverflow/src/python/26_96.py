def make_bricks(small_bricks, big_bricks, goal):

  if ( (5*big_bricks + small_bricks) < goal ):  #we can't reach the length

    return False

  elif  (small_bricks < (goal%5)) :   #we can surpass the length but we don't have 
                                      #enough 1s to fill goal's residual w.r.t. 5 div
    return False

  else:      #We can reach the length and have enough 1s to fill residual

    return True
