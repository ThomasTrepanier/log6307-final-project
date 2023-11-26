from dis import dis

def a():
    squares = (*map((2).__rpow__, range(5)),)
    # print(squares)

print(dis(a))
