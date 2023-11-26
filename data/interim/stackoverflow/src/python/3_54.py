import sys, os

def file_len(fname):
    if os.stat(file_path).st_size == 0:
        print('File is empty')
        return 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len(sys.argv[1]))
