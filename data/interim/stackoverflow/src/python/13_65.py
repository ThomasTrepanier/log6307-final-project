words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse']

def chains(words, previous_word=None):
    # Consider an empty sequence to be valid (as a "tail" or on its own):
    yield []
    # Remove the previous word, if any, from consideration, both here and in any subcalls:
    words = [word for word in words if word != previous_word]
    # Take each remaining word...
    for each_word in words:
        # ...provided it obeys the chaining rule
        if not previous_word or each_word.startswith(previous_word[-1]):
            # and recurse to consider all possible tail sequences that can follow this particular word:
            for tail in chains(words, previous_word=each_word):
                # Concatenate the word we're considering with each possible tail:
                yield [each_word] + tail  

all_legal_sequences = list(chains(words))  # convert the output (an iterator) to a list
all_legal_sequences.sort(key=len) # sort the list of chains in increasing order of chain length
for seq in all_legal_sequences: print(seq)
# The last line (and hence longest chain) prints as follows:
# ['hedgehog', 'giraffe', 'elephant', 'tiger', 'racoon']
