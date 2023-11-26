def expanding(l):
 for i in range(0,len(l)-2):
  if (abs(l[i+2]-l[i+1])>abs(l[i+1]-l[i])):
   Answer=True
  else:
   Answer=False
   return Answer
 return Answer

expanding([1,3,7,2,-3]) 
