from glob import glob, escape
import os
import time


def get_file_count(directory: str) -> int:
    count = 0
    for filename in glob(os.path.join(escape(directory), '*')):
        if os.path.isdir(filename):
            count += get_file_count(filename)
        else:
            count += 1
    return count

start = time.perf_counter()
count = get_file_count('/Volumes/G-DRIVE Thunderbolt 3')
end = time.perf_counter()

print(count)
print(f'{end-start:.2f}s')
