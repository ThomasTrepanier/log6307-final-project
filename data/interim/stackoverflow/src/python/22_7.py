def anti_vowel(text):
    all_vowels = ["A", "E", "U", "I", "O", "a", "e", "o", "u", "i"]
    listed_text = []
    for letter in text:
        listed_text.append(letter)
    for vowel in all_vowels:
        while vowel in listed_text:
            listed_text.remove(vowel)
    return "".join(listed_text)
    
print(anti_vowel("Hey look Words!"))
