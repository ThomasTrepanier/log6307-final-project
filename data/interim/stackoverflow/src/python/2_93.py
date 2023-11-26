def collatz(n):
    sequence = []
    while (n>=1):
        if n in sequence:
            break
        else:
            sequence.append(n)
            if (n==1):
                break # solution is found
            elif (n%2==0):
                n = n/2
            else:
                n = 3*n+1
    return(sequence)
