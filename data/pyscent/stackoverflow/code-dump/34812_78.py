
num = [1, 2, 3, 17, 1, 3, 5, 4, 3, 7, 5, 6, 9]
new = []
def check_nums(x):
    idx = 0
    while idx < len(x) and x[idx] != 7:
        print(idx)
        new.append(x[idx])
        idx += 1
    print(idx)
    return new
print(check_nums(num))

