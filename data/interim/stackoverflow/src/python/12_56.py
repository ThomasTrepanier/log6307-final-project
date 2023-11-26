from numpy import *
def f(x):     #these are all the same function using different identities  
   a = (1-(sin(x)/tan(x)))/(x**2)
   b = (1-(sin(2*x)/(2*sin(x))))/(x**2)
   c = (1-((1-((tan(x/2))**2))/(1+(tan(x/2))**2)))/(x**2)
   d = (sin(x)**2+cos(x)**2-cos(x))/(x**2)
   e = (sin(x)**2+cos(x)**2-(sin(2*x)/(2*sin(x))))/(x**2)
   return a, b, c, d, e
print(f(float128(1.2e-8)))
