def multiply1(*args):    
    # Multiply elements one by one 
    result = 1
    for x in args: 
         result = result * x  
    return result  
print(multiply1(1,2,4))
