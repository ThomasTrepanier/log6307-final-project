def digitoflife(date):
    if len(date) > 8:
        print("date inputed is long")
    else:
        num = num2 = 0
        for digit in date:
            num += int(digit)
        for i in str(num):
                num2 += int(i)
        return num2
date = str(input('Enter the date: '))
print("The digit of life is: ",digitoflife(date))
