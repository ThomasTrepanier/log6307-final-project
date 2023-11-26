def get_number():
    return int(input("Enter an integer: "))

secret_number = 777

number = get_number()
while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = get_number()      

print("Well done, muggle! You are free now.")
