def seriesrun(x, n):
    result = 0
    term = 1

    for _ in range(n):
        result += term
        term *= -x  # -x == 1 * -x, x^2 == (-x) * (-x), -x^3 == x^2 * (-x), etc
    return result
