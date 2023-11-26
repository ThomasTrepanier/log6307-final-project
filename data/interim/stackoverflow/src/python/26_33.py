a=[1,2,3,4,5]
s=2
def rotateList(arr,d,n):
  arr[:]=arr[d-1:n]+arr[0:d-1]
  return arr

print(rotateList(a,5,len(a)))
