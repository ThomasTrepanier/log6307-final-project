import random

def next_input():
    return random.randint(1, 100)

if __name__ == '__main__':
    while True:
        studentScore = next_input()
        print(f"score: {studentScore:3}")
