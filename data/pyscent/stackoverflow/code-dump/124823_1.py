def calculate():
    while True:
        operator = input("What operator do you wanna use(*,/,+,-)? ")
        possible_op = "+-*/"

        if operator not in possible_op:
            continue
        try:
            number_1 = float(input("What is your first number? "))
            number_2 = float(input("What is your second number? "))
        except ValueError:
            continue
    
        if operator == "+":
            print(number_1 + number_2) 
        elif operator == "-":
            print(number_1 - number_2) 
        elif operator == "*":
            print(number_1 *  number_2) 
        elif operator == "/":
            print(number_1 / number_2) 
        break
