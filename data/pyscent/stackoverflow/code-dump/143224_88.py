def is_perfect_square(x):
    i = 1
    while i*i < x:
        i += 1
    return i*i == x

print(is_perfect_square(15))
# False
print(is_perfect_square(16))
# True
