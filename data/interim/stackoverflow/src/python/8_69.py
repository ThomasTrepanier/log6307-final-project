def fx(x):
    v = float(x*x*x - 5*x - 7)
    return v


err = int(input("Enter zeroes in approxiamtion in solution: "))
b = float(input("Enter upper limit for root: "))
a = float(input("Enter lower limit for root: "))
c = 0.0

while abs(fx(c)) > ( 10 ** -err):
    try:
        c = b - ((b - a)/(fx(b) - fx(a))) * fx(b)
    except ZeroDivisionError:
        break
    print(a, b, c, sep=', ')
    a = b
    b = c
    c = 0
    print()
print("The root is approximately = ", b)
