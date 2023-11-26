def n_elements_per_call(iterable, n=100):
    buffer = []
    for i in iterable:
        buffer.append(i)
        if len(buffer) < n:
            continue
        yield buffer
        buffer.clear()
    if buffer:
        yield buffer

my_list = list(range(959))
for nums in n_elements_per_call(my_list):
    print(nums)

