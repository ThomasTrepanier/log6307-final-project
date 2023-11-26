def get_mult_num(given_list):
    multiplies_to_20 = (
        (i, j) for i, j in combinations(given_list, 2)
        if i * j == 20)
    return next(multiplies_to_20, None)
