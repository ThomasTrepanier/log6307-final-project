import re

def count_zeros(number: int) -> int:
    count = re.search(r'0+$', str(number))
    return len(count[0]) if count else 0

print(count_zeros(1))
print(count_zeros(123))
print(count_zeros(0))
print(count_zeros(10))
print(count_zeros(12300))
print(count_zeros(123000))
