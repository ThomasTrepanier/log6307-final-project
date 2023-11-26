x = ['ABC','GOOGLE','BCD','GOOGLY', 'A','A']
def make_object(arr):
  lengths = (len(item) for item in arr);
  obj = {}
  for item in lengths:
    obj[item] = obj[item] + 1 if item in obj else 1
  return obj

make_object(x)
