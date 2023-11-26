def sms_encoding(data):

    data=data.lower()
    a=data.split()
    v1=""
    for i in range(0,len(a)):
        z=a[i]
        v=""
        c1=0
        for j in z:
            if j not in ('a','e','i','o','u'):
                v=v+j
            elif j in ('a','e','i','o','u'):
                c1=c1+1
        if(c1!=len(z)):    
            v1=v1+v+" "
        elif(c1==len(z)):
            v1=v1+z+" "
    
    word=v1[0:len(v1)-1]
    return word

data="I love Python"
print(sms_encoding(data))
