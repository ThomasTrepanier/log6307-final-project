from bisect import bisect_left, insort_left

n, d = map(int, input().split())
t = list(map(int, input().split()))
noti = 0

listD = sorted(t[:d])

def median():
  return listD[d//2] if d%2 == 1 else ((listD[d//2] + listD[d//2-1])/2)

for i in range(d,n):
  if t[i] >= 2*median(): noti += 1
  del listD[bisect_left(listD, t[i-d])]
  insort_left(listD, t[i])
print(noti)
