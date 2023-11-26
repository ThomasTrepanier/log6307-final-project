word = 'yoyo'

def vocals_consonants_transformation(word):
    modified_word = ""
    for i in range(0, len(word)):
        if word[i].isalpha():
            if word[i] in "aeiou":
                modified_word += 'v'
            else:
                modified_word += 'c'
        else:
            modified_word += word[i]
    return modified_word


print(vocals_consonants_transformation(word))
