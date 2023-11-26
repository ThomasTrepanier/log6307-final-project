import random

total = 0
diceRollList = []

# Define dice rolling function
def rollDice():
    rollResult = random.randint(1, 6)
    if rollResult == 6:
        # If 6 Rolled run two more rolls and sum the results
        print("Rolled a 6 Rolling 2 more")
        return sum([rollDice() for _ in range(2)])
    # If 6 not rolled return the result
    print(f"Rolled a {rollResult}")
    return rollResult

while True:

    numberOfDice = int(input("How many Die to throw: "))

    if numberOfDice not in range(1, 6):
        print("Number of dice should be between 1 and 5")
        break

    for dice in range(numberOfDice):
        print(f"Rolling Dice {dice}")
        # Add result to the total
        total += rollDice()
        print(f"Running Total: {total}")
