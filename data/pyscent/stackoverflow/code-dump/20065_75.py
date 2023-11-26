def one():
  l = [1,8,8,8,1,3,3,8]
  count={}
  res=[]
  for i in l:
    if i in count: count[i]+=1
    else: count[i]=1
    if count[i]%2: res.append(i)

  #print(res)


def two():
  from collections import Counter
  l = [1,8,8,8,1,3,3,8]
  res = []
  count = Counter(l) # its like dict(1: 2, 8: 4, 3: 2)
  for key, val in count.items():
    res.extend(val//2 * [key])

o=timeit.Timer(one)

t=timeit.Timer(two)

print(o.timeit(100000))

print(t.timeit(100000))

print(o.timeit(100000))

print(t.timeit(100000))
