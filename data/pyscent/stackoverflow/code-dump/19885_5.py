def float_swap(x):
    return f"{x % 1 * 10:.0f}.{x:.0f}"

print(float_swap(2.5))
print(float_swap(37))
