import itertools

file_name = 'sample.txt'
d = {}
expected_lines = 5

def grouper(iterable, n, fillvalue=''):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

def check_empty(int_pairs):
    int_pairs = int_pairs.split()
    if len(int_pairs) > 1:
        return int_pairs
    else:
        return []

with open(file_name, 'r') as f:
    blocks = list(grouper(f, expected_lines, fillvalue=''))

for block in blocks:
    lines = [i.replace('\n','') for i in block if i][:expected_lines-1]
    d[int(lines[0])] = (lines[1],check_empty(lines[2]),check_empty(lines[3]))
