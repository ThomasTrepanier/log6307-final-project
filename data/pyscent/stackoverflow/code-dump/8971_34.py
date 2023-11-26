import timeit
import random


def increasing_sequence_pos(sequence):
    for n, (a, b) in enumerate(zip(sequence[:-1], sequence[1:])):
        if a >= b:
            return False, n + 1
    return True, -1


def almost_increasing_sequence(sequence):
    increasing, n = increasing_sequence_pos(sequence)
    return (
        # either it was already increasing
        increasing or
        # or the problem is with the last element
        n == len(sequence)-1 or
        ((
            # or the first element was the problem 
            n == 1
            # or the element at position n was the problem
            (sequence[n - 1] < sequence[n + 1]) or
            # or the element at position n-1 was the problem
            (sequence[n - 2] < sequence[n] < sequence[n + 1])
        ) and increasing_sequence_pos(sequence[n:])[0])
    )


size = 1000000

# time on simple increasing series
numbers = list(range(size))
print(timeit.timeit(lambda: almost_increasing_sequence(numbers), number=1))
print(f'Result: {almost_increasing_sequence(numbers)}')

# time on single issue
numbers[random.randint(1, size)] = 0
print(timeit.timeit(lambda: almost_increasing_sequence(numbers), number=1))
print(f'Result: {almost_increasing_sequence(numbers)}')

# time on two issues issue
numbers[random.randint(1, size)] = 0
print(timeit.timeit(lambda: almost_increasing_sequence(numbers), number=1))
print(f'Result: {almost_increasing_sequence(numbers)}')
