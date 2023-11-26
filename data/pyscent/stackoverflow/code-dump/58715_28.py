def myfunc(arr):
 ignore_list = []
 newlist = []
 for i,v in enumerate(arr):
     if v >= 6 and v <= 9:
         ignore_list.append(i)
     if i in ignore_list:
         newlist.append(0)
     else:
         newlist.append(v)

 return sum(newlist)
