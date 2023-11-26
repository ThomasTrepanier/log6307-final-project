
def my_func(list1, list2):
    count = 0
    for i in list1:
        for j in list2:
            if(i == j) : count += 1
    print(count)
    if(count >= 2) : return True
    else: return False


list1 = ["a", "b", "c"]
list2 = ["a", "f", "g", "b"]

if my_func(list1, list2):#list2 contains any 2 elements of list1:
    print("yes, list 2 contains 2 elements of list 1")
else:
    print("no, list 2 does not contain 2 elements of list 1")
