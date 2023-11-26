T = int(input())
for test in range(T):
    house = []
    input1 = input()
    input1 = input1.split()
    N = int(input1[0])
    B = int(input1[1])
    input2 = input()
    input2 = input2.split()
    for x in input2:
        price = int(x)
        dictionary = {"house":x,"price":price}
        house.append(dictionary)
    
    def myFunc(e):
        return e['price']

    house.sort(key=myFunc)

    spent = 0
    purchased = 0

    for x in house:
        variable1 = x.get('price')
        spent += variable1
        if spent <= B:
            purchased += 1

    print(f"Case #{test+1}: {purchased}")
