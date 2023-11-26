import copy
def rotateImage(a):
 out = copy.deepcopy(a)
 x = 0;
 y = 0;
 for i in a:
  l = len(i)
  for j in i:
   out[y][x+l-1] = j
   y += 1
   if(y == l):
    y=0
  x -= 1
 return(out)
