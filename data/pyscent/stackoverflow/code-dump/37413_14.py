def powrange(*args, base=10):
    for i in range(*args):
        yield base ** i


for i in powrange(2, -1, -1, base=10):
    print(i)
# 100
# 10
# 1
