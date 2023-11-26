def fizz_buzz(self):
    if number_value % 3 == 0 and number_value % 5 == 0:
        print("FizzBuzz")
    elif number_value % 3 == 0:
        print("Fizz")
    elif number_value % 5 == 0:
        print("Buzz")
    else:
        return f"{number_value} can't be multiplied by either 3 or 5"
