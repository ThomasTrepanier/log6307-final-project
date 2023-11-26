def to_bin(l):
    val, length = l
    bit_str = ''.join(bin(ord(i)).replace('0b', '') for i in val)
    if len(bit_str) < length:
        # pad with zeros
        return '0'*(length-len(bit_str)) + bit_str
    else:
        # cut to size
        return bit_str[:length]

bytes_val = [b'\x80\x00',14]
print(to_bin(bytes_val))
