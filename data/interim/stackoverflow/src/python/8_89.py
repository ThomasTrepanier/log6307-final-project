def intersection(list1, list2): 
     lst3 = [value for value in list1 if value in list2] 
     return lst3 


list1 = ["a", "b", "c"]
list2 = ["a", "f", "g", "b"]

if len(intersection(list1, list2) == 2):
    print("yes, list 2 contains 2 elements of list 1")
else:
    print("no, list 2 does not contain 2 elements of list 1")
