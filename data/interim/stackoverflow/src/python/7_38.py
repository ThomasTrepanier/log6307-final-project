def bytest_to_bit(by, n):
    bi = "{:0{l}b}".format(int.from_bytes(by, byteorder='big'), l=len(by) * 8)[:n]
    return ' '.join([bi[i:i + 8] for i in range(0, len(bi), 8)])

bytest_to_bit(b'\xff\xff\xff\xff\xf0\x00', 45)
