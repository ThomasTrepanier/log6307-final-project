def recursive_function(n):
    if n <= 0:
        return
    print(n)
    recursive_function(n - 1)

recursive_function(5)
# Output:
# 5
# 4
# 3
# 2
# 1
