def power_of_two(n):
    count = 0
    st = str(bin(n))
    st = st[2:]

    for i in range(0,len(st)):
        if(st[i] == '1'):
            count += 1
        
    if(count == 1):
        print("True")
    else:
        print("False")
