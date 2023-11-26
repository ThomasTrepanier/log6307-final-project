Group_A = ['nice','car','by','shop']
Group_B = ['no','thing','great']

from collections import defaultdict

group_a=defaultdict(int)
group_b=defaultdict(int)

for i in Group_A:
    group_a[i]=1

for i in Group_B:
    group_b[i]=1

t_string_A = 'there is a car over there'
t_string_B = 'no one is in a car'

def fun2(string):
    l=[]
    past=0
    for i in range(len(string)):
        if string[i]==' ':
            if string[past:i]!='':
                l.append(string[past:i])
            past=i+1
    return l

def fun(string,dic):
    for i in fun2(string):
   # for i in string.split():
        try:
            if dic[i]:
                return 1
        except:
            pass
    return 0

if fun(t_string_A,group_a)==fun(t_string_B,group_b):
    print(1)
else:
    print(0)
