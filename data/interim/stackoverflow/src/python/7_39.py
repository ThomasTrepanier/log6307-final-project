def bytest_to_bit(by, n):
    bi = ' '.join(map('{:08b}'.format, by))
    return bi[:n + len(by) - 1].rstrip()

bytest_to_bit(b'\xff\xff\xff\xff\xf0\x00', 45)
