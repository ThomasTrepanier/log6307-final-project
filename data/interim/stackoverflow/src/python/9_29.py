def my_fancy_test(my_list):
    pattern = ['a', 'b']
    if not len(my_list) % len(pattern) == 0:
        return False
    for i in range(0, len(my_list)):
        if not my_list[i] == pattern[i % len(pattern)]:
            return False
    return True
