def add_between_numbers(num1:int,num2:int):
    sum = num1 + num2
    for i in range(num1 - num2):
        if i >=1:
            sum += (num2 + i)
    print(sum)
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1>num2:
    add_between_numbers(num1,num2)
else:
    add_between_numbers(num2,num1)
