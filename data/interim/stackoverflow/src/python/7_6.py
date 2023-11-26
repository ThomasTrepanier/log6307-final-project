import re
def word_with(word, char):
    word_string = word.split()
    print(word_string)
    word_with = [x for x in word_string if re.search(r'^[s]',x,re.I)]
    return(word_with)

word = "She sells seashells by the seashore"
print(word_with(word,'s'))
