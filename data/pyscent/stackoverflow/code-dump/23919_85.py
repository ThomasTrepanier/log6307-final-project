def convert(i):
    output = ''
    pos = 0
    while i:
        if i & 1:
            output += 'ABCDE'[pos]
        pos += 1
        i >>= 1
    return output
