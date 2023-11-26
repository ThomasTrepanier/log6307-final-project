import itertools
def f(lst,num):
    for x,y in itertools.combinations(lst,2):
        if x+y==num:
            return True
    return False
lst=[1,2,3]
num=int(input("Give me a number: "))
print(f(lst,num))
