from timeit import repeat
import re
import tracemalloc as tm

def swap_words_split(s, x, y):
    return y.join(part.replace(y, x) for part in s.split(x))

def swap_words_regex1(s, x, y):
    return re.sub(re.escape(x) + '|' + re.escape(y),
                  lambda m: (x if m[0] == y else y),
                  s)

def swap_words_regex2(s, x, y):
    return re.sub(f'({re.escape(x)})|{re.escape(y)}',
                  lambda m: x if m[1] is None else y,
                  s)

def swap_words_replaces(s, x, y):
    return s.replace(x, chr(0)).replace(y, x).replace(chr(0), y)

funcs = swap_words_split, swap_words_regex1, swap_words_regex2, swap_words_replaces

args = 'apples and avocados and bananas and oranges and ' * 10000, 'apples', 'avocados'

for _ in range(3):
    for func in funcs:
        t = min(repeat(lambda: func(*args), number=1))
        tm.start()
        func(*args)
        memory = tm.get_traced_memory()[1]
        tm.stop()
        print(f'{t * 1e3:4.1f} ms  {memory // 1000:4} kB  {func.__name__}')
    print()
