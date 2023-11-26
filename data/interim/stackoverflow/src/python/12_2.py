def count_even_digits_spyr03_for(n):
    count = 0
    for c in str(n):
        if c in "02468":
            count += 1
    return count
