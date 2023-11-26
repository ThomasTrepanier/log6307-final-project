funcs = []
for i in range(4):
  def f(num=i):
    print(num)
  funcs.append(f)
