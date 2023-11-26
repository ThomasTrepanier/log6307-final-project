lst = [1, 2, 3, 4, 5, 6, 7, 8]
sliding_window_size = 3

def get_sliding_list(l, index):
    l_list = []
    r_list = []

    min_range = 0
    if index > sliding_window_size:
        min_range = index - sliding_window_size

    max_range = len(l)
    if index + sliding_window_size < len(l):
        max_range = index + sliding_window_size + 1

    return (l[min_range:index], l[index + 1:max_range])

print(get_sliding_list(lst, 0))
print(get_sliding_list(lst, 1))
print(get_sliding_list(lst, 2))
print(get_sliding_list(lst, 3))
print(get_sliding_list(lst, 4))
print(get_sliding_list(lst, 5))
print(get_sliding_list(lst, 6))
print(get_sliding_list(lst, 7))
