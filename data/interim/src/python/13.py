def next_braille_representation(current_rep):
    braille_sequence = "100000101000110000110100100100111000111100101100011000011100100010101010110010110110100110"
    index = braille_sequence.find(current_rep)

    if index != -1 and index < len(braille_sequence) - 6:
        next_rep = braille_sequence[index + 6: index + 12]
    else:
        next_rep = None

    return next_rep
