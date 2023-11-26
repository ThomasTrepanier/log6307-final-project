def get_codon_list(codon_string):
    codon_length = 3

    codon_list = [codon_string[x:x+codon_length] for x in range(0, len(codon_string), codon_length)]

    return codon_list
