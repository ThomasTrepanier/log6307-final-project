def float_swap(x):
    ix = int(x)
    if x == ix:
        return f"0.{ix}"
    return '.'.join(str(x).split(".")[::-1])

print(float_swap(2.5))

print(float_swap(37))
