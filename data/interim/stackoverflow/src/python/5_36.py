def fibonacci(a):
    ls = [1, 1]
    for i in range(2, a):
        ls.append(ls[i - 1] + ls[i - 2])
    return ls[-1]

# 21
print(fibonacci(8))
