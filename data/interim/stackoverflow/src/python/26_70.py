def mult(m, n):
    result = sum(m for _ in range(abs(n)))
    if n < 0:
        return -result
    else:
        return result


m = int(input())
n = int(input())
print(mult(m, n))

