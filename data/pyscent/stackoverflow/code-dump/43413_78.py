from itertools import permutations

def continuous_starting_sequence(words):
    chain = [words[0]]
    for i in range(1, len(words)):
        if not words[i].startswith(words[i - 1][-1]):
            break
        chain.append(words[i])
    return chain

words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse']
best = max((continuous_starting_sequence(seq) for seq in permutations(words)), key=len)

print(best)
# ['hedgehog', 'giraffe', 'elephant', 'tiger', 'racoon']
