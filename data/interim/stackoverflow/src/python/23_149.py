def issumoftwo(lst,num):
    for x in lst:
        for y in lst:
            if x+y==num and lst.index(x)!=lst.index(y):
                return True
    return False
lst=[1,2,3]
num=int(input("Give me a Number: "))
print(issumoftwo(lst,num))
