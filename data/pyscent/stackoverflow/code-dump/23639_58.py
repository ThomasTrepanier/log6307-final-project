#!/usr/bin/env python3
def Checkdiv(n, d):
    r =int(n % d)
    if r==0:
        return (True,r)
    else:
        return (False,r)
n= int(input('Please enter the number to evaluate:'))
d= int(input('Please enter the divisor: '))

bool, num = Checkdiv(n,d)

if bool is True :
    print(f'{n} can be divided by {d} since the end remainder is {num}')
else: 
    print (f'{n} cannot be divided by {d} since remainder is {num}')
