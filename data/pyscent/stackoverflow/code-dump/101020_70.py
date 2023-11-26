def pig_latin(text):
    words = [
        word[1:] + word[0] + "ay"
        for word in text.split()
    ]
    return " ".join(words)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay n
