from functools import reduce
# Python3 program to multiply all values in the 
# list using lambda function and reduce()  
def multiply3(*args):      
    return reduce((lambda x, y: x * y), args)  
print(multiply3(1,2,4))
