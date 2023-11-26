def function5():
    inner_sum = float()
    result = float()

    for x in range(0, n + 1):
        inner_sum += x
        result += x ** 2 * inner_sum
        
    return result
