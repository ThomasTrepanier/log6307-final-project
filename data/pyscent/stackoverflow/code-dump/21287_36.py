from collections import deque
from itertools import chain, repeat, starmap
import os  

def bit_lenght_list(n):
    eights, rem = divmod(n, 8)
    return chain(repeat(8, eights), (rem,))


def build_bitstring(byte, bit_length):
    d = deque("0" * 8, 8)
    d.extend(bin(byte)[2:])
    return "".join(d)[:bit_length]


def bytes_to_bits(byte_string, bits):
    return "{!r}B".format(
        " ".join(starmap(build_bitstring, zip(byte_string, bit_lenght_list(bits))))
    )
