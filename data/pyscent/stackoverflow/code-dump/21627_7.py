def word_with(word, char):
    char_lower = char.lower()
    word_string = word.split()
    word_with = [x for x in word_string if char_lower in x.lower()]
    return(word_with)


word = "She sells seashells by the seashore"
print(word_with(word, "s"))
