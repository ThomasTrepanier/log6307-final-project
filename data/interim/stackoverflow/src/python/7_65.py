def get_codon_list(codon_string):
    codon_length = 3
    codon_list = []

    for codon_start in range(0, len(codon_string), codon_length):
        codon_end = codon_start + codon_length
        codon_list.append(codon_string[codon_start:codon_end])

    return codon_list
