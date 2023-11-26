def count_letters(text):
    result = {}
    text = text.lower().replace(" ","")
    text = text.replace("", " ").split()
    dummy = []
    dummy1 = ""

    for x in text: # remove non-letter
        if x.isalpha():
            dummy.append(x)
            dummy1 = "".join(dummy)

    for letter in dummy1:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("AaBbCc"))
print(count_letters("Math is fun! 2+2=4"))
print(count_letters("This is a sentence."))
