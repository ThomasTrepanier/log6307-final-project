import numpy as np


def generate_answer(n: int, low_limit:int, high_limit: int):
    while True:
        a = np.random.randint(low_limit, high_limit + 1, 1)[0]
        b = np.random.randint(low_limit, high_limit + 1, 1)[0]
        c = (n - 7 * a - 5 * b) / 3.0
        if int(c) == c and low_limit <= c <= high_limit:
            break

    return a, b, int(c)


if __name__ == "__main__":
    n = 30
    ans = generate_answer(low_limit=-5, high_limit=50, n=n)
    assert ans[0] * 7 + ans[1] * 5 + ans[2] * 3 == n
    print(ans)
