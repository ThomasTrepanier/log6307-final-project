def digits(x,N):
    return int((abs(x) % 1) * 10**N)
    
print(digits(1.23456,2))
print(digits(-1.23456,3))
print(digits(1.23,5))
