def func(x,y):
    sum = 0

    #Loop for adding
    for i in range(x,y+1):
        sum+=i

    #Loop for printing
    for i in range(x,y+1):
        if i == y:
            print(i,end = '')
        else: print(i," + ",end = '')
    print(" = ",sum)
