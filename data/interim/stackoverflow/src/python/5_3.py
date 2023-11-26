def float_swap(x): # 2.5
    a = x - int(x) # a = 2.5 - 2 = 0.5
    b = int(x)     # b = 2
    return str(b+a)# str(2 + 0.5)

print(float_swap(2.5))
# 2.5 
