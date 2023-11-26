def RearrangeNumbers(source):
    tmp0=source.split()
    int_l=[]
    for j,i in enumerate(tmp0):
      try:
        tmp0[j]=int(i)
        int_l.append(int(i))
      except ValueError:
        pass
    int_l.sort()
    for j,i in enumerate(tmp0):
      if isinstance(i,int):
        tmp0[j]=str(int_l[0])
        int_l.pop(0)
    return ' '.join(tmp0)

print(RearrangeNumbers(input()))
