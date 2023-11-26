def digits(num):
    while num:
        yield num % 10
        num //= 10

def check(num):
    num = list(digits(num))
    num.reverse()
    for i, j in zip(islice(cycle(range(10)), num[0], num[0] + len(num)), num):
        if i != j:
          return False
    return True
