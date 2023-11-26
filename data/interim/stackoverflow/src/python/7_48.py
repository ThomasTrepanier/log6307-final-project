import time
start_time = time.time()
bits = [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0] * 100000
    ### tested code ###
print("Execution time: ", time.time() - start_time, "seconds")


### former solution --> 0.59 seconds
out_str = ""
for i in range(0,len(bits),8):
    x=bits[i:i+8]
    l="".join([str(j) for j in x[::-1]])
    out_str += chr(int(("0b"+l),base=2))


### enumerate and result.append --> 0.48 seconds
result = []
c = 0
for i,v in enumerate(bits):
    i = i % 8
    c = c | v << i
    if i == 7:
        result.append(chr(c))
        c = 0
out_str = ''.join(result)


### sum and enumerate --> 0.45 seconds
out_str = ""
for item in [bits[i:i + 8] for i in range(0, len(bits), 8)]:
    out_str += chr(sum(x<<i for i,x in enumerate(item)))


### map and chars dictionary --> 0.10 seconds
chars = { tuple(map(int,f"{n:08b}"[::-1])):chr(n) for n in range(0,256) }
def toChars(bits):
    return "".join(chars[tuple(bits[i:i+8])] for i in range(0,len(bits),8) )


### bytes and zip --> 0.06 seconds
chars = { tuple(map(int,f"{n:08b}")):n for n in range(256) }
def toChars(bits):
    return bytes(chars[b] for b in zip(*(bits[7-i::8] for i in range(8)))).decode()
