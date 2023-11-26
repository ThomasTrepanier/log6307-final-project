def order(sentence):
    words = sentence.split()
    ordered_words = sorted(words, key=int_from_word)
    return " ".join(ordered_words)

def int_from_word(word):
    for character in word:
        if character.isdigit():
            return int(character)
    return None

print(order("is2 Thi1s T4est 3a"))
