bits = [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0]

chars = { tuple(map(int,f"{n:08b}"[::-1])):chr(n) for n in range(0,256) }

def toChars(bits):
    return "".join(chars[tuple(bits[i:i+8])] for i in range(0,len(bits),8) )
