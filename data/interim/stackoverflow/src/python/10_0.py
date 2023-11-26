import random

def take_random_5(l):
    randword = random.choice(l)
    if len(randword) != 5:
        return 
    return randword

words = r"C:\users\Cece\words.txt" 
lines = [line.rstrip('\n') for line in open(words)]
while True:
    take_random_5(lines)
