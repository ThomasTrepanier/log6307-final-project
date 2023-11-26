def nextprime(n):
    if n < 0:
      raise ValueError
  
    for i in range(n + 1, n +200):
        if i > 1:
            pr = True
            for j in range(2, i):
                if (i % j) == 0:
                    pr = False
                    break
            if pr:
                return i
    return 'not found'
