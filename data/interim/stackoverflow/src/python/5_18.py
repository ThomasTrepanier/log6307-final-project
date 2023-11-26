def generate_all_answers(n: int, low_limit:int, high_limit: int):
    results = []
    for a in range(low_limit, high_limit + 1):
        for b in range(low_limit, high_limit + 1):
            c = (n - 7 * a - 5 * b) / 3.0
            if int(c) == c and low_limit <= c <= high_limit:
                results.append((a, b, int(c)))

    return results
