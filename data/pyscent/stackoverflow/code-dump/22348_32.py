def swapfirstlast(x):
   if len(x) == 1:
      return x
   else:
     return x[-1:] + x[1:-1] + x[:1]

In [3532]: swapfirstlast('a')                                                                                                                                                                  
Out[3532]: 'a'

In [3533]: swapfirstlast('code')                                                                                                                                                               
Out[3533]: 'eodc'

In [3534]: swapfirstlast('ab')                                                                                                                                                                 
Out[3534]: 'ba'


