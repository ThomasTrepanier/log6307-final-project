import itertools

data = [
    (1, 0, 5),
    (2, 4, 2),
    (3, 2, 1),
    (4, 3, 4),
    (3, 3, 1),
    (1, 2, 2),
    (4, 0, 3),
    (0, 3, 5),
    (1, 5, 1),
    (1, 5, 2),
]

def dissimilar(t1, t2):
    if t1 and t2:
        a, b, c = t1
        x, y, z = t2
        return (a != x) + (b != y) + (c != z)
    return 0

def score(data):
    return sum(dissimilar(t1, t2) for t1, t2 in zip(data, data[1:]))

def solve(data):
    def solve(head, data, tail):
        if len(data) <= 3:
           perm = min(itertools.permutations(data),
                      key=lambda perm: score([head, *perm, tail]))
           return list(perm), score([head, *perm, tail])
        half = len(data) // 2
        result = result_score = None
        for center in list(data):
            data.remove(center)
            for left in itertools.combinations(data, half):
                left = set(left)
                right = data - left
                left, score_left = solve(head, left, center)
                right, score_right = solve(center, right, tail)
                if result_score is None or score_left + score_right < result_score:
                    result = [*left, center, *right]
                    result_score = score_left + score_right
            data.add(center)
        return result, result_score
    return solve(None, set(data), None)

result, result_score = solve(data)
print(result, result_score, score(result), sorted(result) == sorted(data))
