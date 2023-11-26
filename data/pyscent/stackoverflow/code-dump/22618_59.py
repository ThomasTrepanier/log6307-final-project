def main():
    M = float(input('Please enter sales for Monday: '))
    T = float(input('Please enter sales for Tuesday: '))
    W = float(input('Please enter sales for Wednesday: '))
    R = float(input('Please enter sales for Thursday: '))
    F = float(input('Please enter sales for Friday: '))
    sales = [M, T, W, R, F]

    total = 0 

    for value in sales:
        total += value
    total = "{0:.2f}".format(total)
    print ('The total sales for the week are: $' + str(total))

main()
