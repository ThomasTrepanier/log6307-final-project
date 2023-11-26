def op(operator,num1,num2):
    global num3
    if operator == "/":
        num3 = num1 / num2
    elif operator == "+":
        num3 = num1 + num2
    elif operator == "-":
        num3 = num1 - num2
    elif operator == "*":
        num3 = num1 * num2
    else:
        print("FATAL ERROR")

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
operator = input("Please enter operator: ")
op(operator,num1,num2)
print(num3)

continue1 =  input ("Would you like too continue? [Yes/No]").lower()

if continue1 in ["yes", "y"]:
    num4 = float(input("Please enter second number: "))
    operator = input("please enter operator")
    op(operator,num3,num4)
    print(num3)
else:
    print("Fatal error")

input("Press Enter to Exit")
