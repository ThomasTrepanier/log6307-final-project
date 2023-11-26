def myfunc(x):
   seq = []
   for i, v in enumerate(x):
      seq.append(v.upper() if i % 2 == 0 else v.lower())
   return ''.join(seq)
