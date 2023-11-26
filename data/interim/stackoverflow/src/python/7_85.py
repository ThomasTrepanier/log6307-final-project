def leadingZeros(number, digits):
    numberString = str(number)
    for digit in range(1, digits):
        if number < 10**digit:
            numberString = '0' + numberString
    return numberString


def autoIncrement(oldNumber):
    order = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!'
    lastDigitOrder = order.find(oldNumber[3])
    newNumber = ''
    if order.find(oldNumber[1]) <= 9:
        # 3 digit number
        number = int(oldNumber[1:]) + 1
        letter = oldNumber[0]
        if 1000 == number:
            letterOrder = order.find(oldNumber[0])
            letter = order[letterOrder + 1]
        newNumber = letter + leadingZeros(number % 1000, 3)
    elif order.find(oldNumber[2]) <= 9:
        # 2 digit number
        number = int(oldNumber[2:]) + 1
        letters = oldNumber[0:2]
        if 100 == number:
            letterOrder = order.find(oldNumber[1])
            letter = order[letterOrder + 1]
            letters = oldNumber[0] + letter
        newNumber = letters + leadingZeros(number % 100, 2)
    elif order.find(oldNumber[3]) <= 9:
        # 1 digit number
        number = int(oldNumber[3]) + 1
        letters = oldNumber[0:3]
        if 10 == number:
            letterOrder = order.find(oldNumber[2])
            letter = order[letterOrder + 1]
            letters = oldNumber[0:2] + letter
        newNumber = letters + leadingZeros(number % 10, 1)
    else:
        # just letters
        print(oldNumber)
        letterOrder = order.find(oldNumber[3])
        letter = order[letterOrder + 1]
        newNumber = oldNumber[0:3] + letter

    # if one of the digits has gone past Z then we need to update the letters
    if '!' == newNumber[3]:
        # past Z in 4th digit
        letterOrder = order.find(oldNumber[2])
        newNumber = newNumber[0:2] + order[letterOrder + 1] + 'A'
    if '!' == newNumber[2]:
        # past Z in 3rd digit
        letterOrder = order.find(oldNumber[1])
        newNumber = newNumber[0:1] + order[letterOrder + 1] + 'A' + newNumber[3]
    if '!' == newNumber[1]:
        # past Z in 2nd digit
        letterOrder = order.find(oldNumber[0])
        newNumber = order[letterOrder + 1] + 'A' + newNumber[2:]

    return newNumber


print(autoIncrement('A999'))
print(autoIncrement('AA99'))
print(autoIncrement('AAA9'))
print(autoIncrement('AAAA'))
print(autoIncrement('AZZ9'))
