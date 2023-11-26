def add_vs_between_not_cons(array):
  iterable = sorted(array, key= lambda x: int(x[1:]))
  i, size = 0, len(iterable)
  while i < size:
    delta = int(iterable[i][1:]) - int(iterable[i-1][1:])
    for _ in range(delta-1):
      yield "V"
    yield iterable[i]
    i += 1
