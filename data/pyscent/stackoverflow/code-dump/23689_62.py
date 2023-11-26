def mul_tup(tup1, tup2):
        l=[]

        for x in tup1:
            for y in tup2:
                a=(x,y)
                b=(y,x)
                l.append(a)
                l.append(b)

        return tuple(l)

first_tup= tuple([eval(x) for x in input("enter the values: ").split(',')])
second_tup= tuple([eval(x) for x in input("enter the values: ").split(',')])
q = mult_tup(first_tup, second_tup)
print(q)
