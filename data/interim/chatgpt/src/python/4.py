def next_braille_representation(current_rep):
    # Convert the current representation to an integer (treated as binary)
    current_int = int(current_rep, 2)

    # Calculate the next integer representation by adding 1
    next_int = current_int + 1

    # Convert the next integer back to a 6-bit binary string
    next_rep = format(next_int, '06b')

    return next_rep

# Example usage:
current_rep = '100000'
next_rep = next_braille_representation(current_rep)  # Output: '100001'
