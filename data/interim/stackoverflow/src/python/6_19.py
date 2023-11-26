def checkRange(number):
    if number in range(0, 5499):
        return 5000
    elif number in range(5500, 9499):
        return 10000
    elif number in range(9500, 44499):
        return (floor((number - 9500)/4000) + 3) * 5000
