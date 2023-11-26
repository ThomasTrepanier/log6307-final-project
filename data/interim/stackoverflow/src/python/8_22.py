def merge(ranges):
  """Given a sorted list of range tuples `(a, b)` merge overlapping ranges."""

  if not(ranges):
     return [];

  if len(ranges) == 1:
    return ranges;

  a, b = ranges[0];
  c, d = ranges[1];

  # eg.: [(1, 10), (20, 30), rest]
  if b < c:
    return [(a,b)] + merge(ranges[1:]);

  # examples: [(1, 5), (2, 3), rest],
  #           [(1, 5), (2, 10), rest]
  return merge([(a, max(b, d))] + ranges[2:]);
