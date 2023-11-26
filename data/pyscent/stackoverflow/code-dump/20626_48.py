def par_nepar(n):
    s,h=0,0
    for i in range(len(n)-1):
        if n[i]%2==0 and n[i+1]%2!=0:
            s+=1
        elif n[i]%2!=0 and n[i+1]%2==0:
            h+=1
    if s==len(n)//2 or h==len(n)//2:
        print("The number complies to the needed terms")
    else:
        print("The number does not complies to the needed terms")

# list of digits in the provided input
n = list(map(lambda x: int(x),list(input("Unesite broj n: "))))
par_nepar(n)
