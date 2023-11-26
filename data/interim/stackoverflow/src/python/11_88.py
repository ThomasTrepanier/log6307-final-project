def main():
    introduction()
    attempt=1
    while attemptValid(attempt) and answerIsWrong(askQuestion(), attempt):
        attempt += 1

def attemptValid(attempt):
    max_attempts=4
    if attempt < max_attempts:
        return 1
    print('You used the maximum number of attempts, sorry. The correct answer is "Madison"')
    return 0

def answerIsWrong(answer, attempt):
    if answer != 'Madison':
        return 1
    print(f"Correct! Thanks for playing. It took you {attempt} attempt(s).")
    return 0

def introduction():
    print('Quiz program!\n')

def askQuestion():
    return input('What is the capital of Wisconsin? ')

main()
