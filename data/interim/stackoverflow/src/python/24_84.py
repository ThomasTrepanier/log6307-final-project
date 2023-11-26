#Import package
import numpy as np

#Define a new function called qes
def qes(a1,b1,c1):

    ans1=((-1*b1)+np.lib.scimath.sqrt((b1**2)-(4*a1*c1)))/(2*a1)
    ans2=((-1*b1)-np.lib.scimath.sqrt((b1**2)-(4*a1*c1)))/(2*a1)

    return ans1,ans2

#With the defined function perform a calculation and print the answer
ans1,ans2=qes(1,2,1)
print('Answer 1 is: ',ans1,' Answer 2 is: ',ans2)
