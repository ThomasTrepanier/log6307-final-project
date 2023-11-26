class MyArray:
  def __init__(self, arr):
    self.arr = arr
  def __getitem__(self, t):
    return self.arr[t[0]][t[1]]

myarr = MyArray([[1,1,1], [1,2,2], [1,2,2]])
print(myarr[0,1])
