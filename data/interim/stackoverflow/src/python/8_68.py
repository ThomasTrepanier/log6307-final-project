def fx(x):
    v = float(x*x*x - 5*x - 7)
    return v


err = int(input("Enter zeroes in approximation in solution: "))
b = float(input("Enter upper limit for root: "))
a = float(input("Enter lower limit for root: "))
c = 0.0
ctr = 0 #                           ^^^^^^^^^^^^^^^^^^
while abs(fx(c)) > (1 * 10 ** -err) and fx(b) != fx(a): # ^ is binary xor!
    ctr += 1
    c = b - ((b - a)/(fx(b) - fx(a))) * fx(b)
    print(ctr, a, b, c, sep=', ')
    a = b
    b = c
    c = 0
    print()
print("The root is approximately = ", b, ' after ', ctr, ' iterations')
input()
