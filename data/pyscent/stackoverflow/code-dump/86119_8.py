def is_prime(number:int):
 check = 0
 for i in range(2,number):
    if number % i == 0:
        check += 1
 if check == 0:
    return True
 else:
    return False

def next_prime(value):
 check = value + 1
 while is_prime(check) is False:
    check += 1
 return check

value = int(input("Insert the number: "))
print(next_prime(value))
