import timeit

num = ''.join(str(i % 10) for i in range(1, 10000001))

def count_simple_sum():
    return sum(1 for c in num)

def count_simple_for():
    count = 0
    for c in num:
        count += 1
    return count


print('For Loop Sum:', timeit.timeit(count_simple_for, number=10))
print('Built-in Sum:', timeit.timeit(count_simple_sum, number=10))
