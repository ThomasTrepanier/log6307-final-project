def f_recursive2(n):
    def f_helper(x):
        if x <= 0:
            return 0
        return x + f_helper(x-2)

    if n % 2 == 0:
        return f_helper(n-1)
    else:
        return f_helper(n-2)
