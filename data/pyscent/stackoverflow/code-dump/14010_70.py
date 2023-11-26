def f(i):
    dq.rotate(-dq.index(i))
    return list(islice(dq, 13))

#  f(90) = [90, 75, 60, 45, 30, 15, 0, 345, 330, 315, 300, 285, 270]
