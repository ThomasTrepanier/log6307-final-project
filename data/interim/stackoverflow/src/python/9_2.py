def required_steps(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    return 1 + 2 * required_steps(n-1)
