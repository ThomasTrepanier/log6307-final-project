sentence = "Mom knock the door"


def is_same_letter_at_begin_end(word):
    return word and word[0].lower() == word[-1].lower()


target_words = list(filter(is_same_letter_at_begin_end, sentence.split()))
print(target_words)
print(len(target_words))
