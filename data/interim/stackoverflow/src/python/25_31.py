def myFun(*args):

    if len(args) == 0:  
        return(0)       
                    
    product = 1
    for arg in args:
        product *= arg
    return(product)


print(myFun())
print(myFun(8, 5))
print(myFun(8, 5, 2))
print(myFun(8, 5, 2, 3))

# Output: 
0
40
80 
240
