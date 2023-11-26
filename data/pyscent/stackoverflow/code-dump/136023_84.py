count = 0
list_num = []

def input_check():
    number = int(input("Enter a positive integer (1-1000). To quit, enter -1: "))
    if number >= 1 and number <= 1000:
        hailstone_game(number)
    elif number == -1:
        return 
    else:
        print("Please type in a number between 1-1000")
        input_check()

def hailstone_game(number):
    global count
    while number != 1:
        count += 1
        list_num.append(number)
        if number % 2 == 0:
            return hailstone_game(int(number/2))
        else:
            return hailstone_game(int(number*3+1))

    list_num.append(1) # cheap uncreative way to add the one
    print(*list_num, sep=" ")
    print(f"The loop executed {count} times.")
    return

input_check()
