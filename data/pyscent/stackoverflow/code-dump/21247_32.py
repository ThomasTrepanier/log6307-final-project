def digital_root(n):
    answ = 0
    s = 0
    x = str(n)
    for i in range(0, len(x)):
        s = s + int(x[i])
    if len(str(s)) > 1:
       s = digital_root(s)
    answ = s # You could even return s directly
    return answ

print(digital_root(493193))
