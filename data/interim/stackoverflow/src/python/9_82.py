def convert(value, tokens=string.ascii_uppercase):
    output = ''
    i = 0
    while value:
        if value & 1:
            output += tokens[i]
        i += 1
        value >>= 1
    return output


def convert2(value, tokens=string.ascii_uppercase):
    return ''.join(tokens[i] for i, c in enumerate(bin(value)[:1:-1]) if c == '1')


def convert3(value, tokens=string.ascii_uppercase):
    result = []
    i = 0
    while value:
        if value & 1:
            result.append(tokens[i])
        i += 1
        value >>= 1
    return ''.join(result)


def convert4(value, tokens=string.ascii_uppercase):
    return ''.join(tokens[pos] for pos in range(value.bit_length()) if value & (1 << pos))


def convert5(value, tokens=string.ascii_uppercase):
    return ''.join(c for b, c in zip(reversed('{:b}'.format(value)), tokens) if b == '1')

print([convert(i) for i in range(16)])
print([convert2(i) for i in range(16)])
print([convert3(i) for i in range(16)])
print([convert4(i) for i in range(16)])
print([convert5(i) for i in range(16)])
print([str(MyBitMask(i)) for i in range(16)])
# ['', 'A', 'B', 'AB', 'C', 'AC', 'BC', 'ABC', 'D', 'AD', 'BD', 'ABD', 'CD', 'ACD', 'BCD', 'ABCD']
