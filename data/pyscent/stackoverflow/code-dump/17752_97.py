def collatz(n):
    sequenceLength = 0
    seen = set()
    while (n>=1):
        if n in seen:
            print("BREAKING NEWS! COLLATZ CONJECTURE DISPROVEN!")
            break
        seen.add(n)
        # remainder of your code
