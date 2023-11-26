def make_combination(letter_positions, chosen_letters, chosen_digits):
    result = [None] * 10
    for letter, position in zip(chosen_letters, letter_positions):
        result[position] = letter
    # Figure out where the digits go, using set arithmetic to find the
    # remaining positions, then putting them back in ascending order.
    digit_positions = sorted(set(range(10)) - set(chosen_letters))
    for digit, position in zip(chosen_digits, digit_positions):
        result[position] = digit
    assert None not in result
    return tuple(result)


def five_letters_and_five_digits():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    # It's not *easy*, but it's fairly elegant.
    # We separately generate the letter positions, letter selection
    # and digit selection, using `product` to get the cartesian product
    # of *those* possibilities; then for each of those, we translate
    # into a desired output - using `starmap` to iterate.
    return itertools.starmap(
        make_combination, 
        itertools.product(
            itertools.combinations(range(10), 5),
            itertools.product(letters, repeat=5),
            itertools.product(digits, repeat=5)
        )
    )
                
