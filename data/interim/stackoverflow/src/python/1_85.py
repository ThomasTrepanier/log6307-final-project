def distribute(oranges, plates):
    base, extra = divmod(oranges, plates) # extra < plates
    if extra == 0:
        L = [base for _ in range(plates)]
    elif extra <= plates//2:
        leap = plates // extra
        L = [base + (i%leap == leap//2) for i in range(plates)]
    else: # plates/2 < extra < plates
        leap = plates // (plates-extra) # plates - extra is the number of apples I lent you
        L = [base + (1 - (i%leap == leap//2)) for i in range(plates)]
    return L
