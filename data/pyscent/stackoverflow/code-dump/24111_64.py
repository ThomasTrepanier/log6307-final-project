def function(n):
    from random import randrange, randint
    mydict = {'key'+str(i):'value1' for i in range(n)}
    mydict['key'+str(randint(0,n-1))] = 'value2'
    return mydict

print(function(5))
