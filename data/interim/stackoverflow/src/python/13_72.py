def printFigure(rows):
    if rows > 0:
        printFigure(rows-1)
        if rows%2 == 0:
            while(rows>0):
                print(str(rows)[::-1], end='')
                rows -= 1
            print('')
        else:
            i = 1
            while (i <= rows):
                print(str(i), end='')
                i += 1
            print('')

printFigure(9)

1
21
123
4321
12345
654321
1234567
87654321
123456789
