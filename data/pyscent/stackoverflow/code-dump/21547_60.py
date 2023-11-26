weight = int(input("Enter your Weight: "))

def getScale(weight):
    return {
        1 : 0.5,
        2 : 1.2,
        3 : 1.7,
        4 : 2.4
    }.get(weight, 0.5)


print(getScale(weight))
