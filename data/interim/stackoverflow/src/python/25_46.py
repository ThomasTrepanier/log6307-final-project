def sum_even_numbers(number):
    if number == 0:
        return 0

    if number % 2 == 0:
        return number + sum_even_numbers(number - 1)  # (number - 2) is also ok
    else:
        return sum_even_numbers(number - 1)
