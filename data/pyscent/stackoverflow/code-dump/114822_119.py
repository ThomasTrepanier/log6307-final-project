def cyclic_perm(a):
    n = len(a)
    b = [[a[i - j] for i in range(n)] for j in range(n)]
    return b

def cyclic_perm_func(a):
    n = len(a)
    def wrapper(a, n, j):
        def cyc():
            return [a[i - j] for i in range(n)]
        return cyc
    b = [wrapper(a, n, j) for j in range(n)]
    return b

a = [1, 2, 3, 4,5,6]
print(cyclic_perm(a))  # Your original function
f = cyclic_perm_func(a) # f is now a list of functions
print([g() for g in f])  # Let's call each in turn
