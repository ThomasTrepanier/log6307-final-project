import itertools

def apple():
  print("In apple")
def mango():
   print("In mango")
def orange():
   print("In orange")

fruits = ['apple','mango','orange']
print(type(fruits))
func = '[%s]'%','.join(map(str,fruits))
print(func) ## [apple,mango,orange]
hehe = eval(func)
print(type(hehe))

n = len(hehe)
func_it = itertools.cycle(hehe)
for i in range(n):
   next(func_it)()
