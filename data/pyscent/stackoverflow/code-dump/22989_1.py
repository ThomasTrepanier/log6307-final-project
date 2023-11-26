import numpy as np

def genrandx():
    # Using a function allows you do to all sorts of crazy stuff and checks.
    x = np.random.randint(1,100)
    x = int((x*.5)**2)
    if (
        (x > 50) and
        (x < 1000) and 
        ( (x%3 == 0) or (x%3 == 0) )
       ): 
        return x 
    else: 
        return genrandx() 

numbers = [ genrandx() for x in range(100)]
print("({}){}".format(len(numbers), numbers))
