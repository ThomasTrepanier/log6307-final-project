def even_sum(n):
    if n%2==0:
        if n==2:
            return 2
        else:
            return(n+even_sum(n-2))
n=10
n*=2
print(even_sum(n))
