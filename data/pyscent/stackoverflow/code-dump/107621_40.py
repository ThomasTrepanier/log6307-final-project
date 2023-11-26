import itertools

def apple():
  print("In apple")
def mango():
   print("In mango")
def orange():
   print("In orange")

func = [apple, mango, orange]  # list of functions
n = len(func)
func_it = itertools.cycle(func)
for i in range(n):
    x = next(func_it)
    print(type(x))  # check the type
    x()
