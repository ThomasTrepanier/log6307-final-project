def sum_of_products(lst, s, f):
    result = 0
    for i, item in enumerate(range(s, f+1)):
        lst[i] = list(map(int, str(item)))
        result += sum(lst[i])
    return result

lst = [x for x in range(0, 10)]
x = sum_of_products(lst, 14, 20)
print(x)
