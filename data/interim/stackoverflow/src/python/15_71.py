def area(length, width):
    return length * width

l = 4
w = 5

print("length =", l, "width =", w, "area =", area(l, w))  # normal way
print(f"length = {l} width = {w} area = {area(l,w)}")     # Same output as above
print("length = {l} width = {w} area = {area(l,w)}")      # without f prefixed
