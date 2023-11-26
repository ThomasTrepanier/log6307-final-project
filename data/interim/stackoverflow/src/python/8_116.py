# your functions
def f0(): print('case 1')
def f1(): print('case 2')
def f2(): print('case 3')
#.
#.
def f15(): print('case 16')

list_of_functions = [f0, f1, f2] # assuming there are 16 functions in total

x = False
y = False
z = False
t = False
total = bin(x + 2 * y + 4 * z + 8 * t)
index = int(total, 2)

list_of_functions[index]() # will print('case 1')

