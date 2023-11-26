def count_zeros(num: int) -> int:
    return len(str(num)) - len(str(num).rstrip('0'))

    

print(count_zeros(0))       #1
print(count_zeros(1))       #0
print(count_zeros(10))      #1
print(count_zeros(245))     #0
print(count_zeros(101))     #0
print(count_zeros(100100))  #2
