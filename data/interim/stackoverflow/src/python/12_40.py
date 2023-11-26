def replace_ending(sentence, old, new):
    if old in sentence:
        sentence = sentence[::-1]
        index = sentence.index(old[::-1])
        new_sentence = sentence[:index] + new[::-1] + sentence[(len(old)+index):]
        return new_sentence[::-1]
    return sentence
