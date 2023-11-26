def next_prime(n):
    while True:
        n=n+1
        for i in range (2,int(n/2)):
            if n%i==0:
                break
        else:
            return n


print(next_prime(67)) 
