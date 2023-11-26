def float_swap(x): # 2.5
    return '.'.join(str(float(x)).split('.')[::-1])

print(float_swap(2.5))
print(float_swap(37))
