lst = [ 7.453511737983394, 
  8.10917072790058, 
  6.2377799380575, 
  5.225853201122676, 
  4.067932296134156 ]

def return_the_num(l, lst, h): 
    return [l if abs(l-x) < abs(h-x) else h for x in lst]

print(return_the_num(3, lst, 9))
# [9, 9, 9, 3, 3]
