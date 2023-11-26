print("Enter two numbers and I will tell you the sum of the numbers.")
print("Press 'q' at anytime to exit.")


def input_number(prompt: str) -> int:
    """Ask the user to input a number, re-prompting on invalid input.
    Exception: raise EOFError if the user enters 'q'."""
    while True:
        try:
            number = input(f"{prompt} number: ")
            if number == 'q':
                raise EOFError
            return int(number)
        except ValueError:
            print("Please enter a number!")


while True:
    try:
        numbers = (input_number(n) for n in ("First", "Second"))
        print(f"The answer is: {sum(numbers)}")
    except EOFError:
        break
