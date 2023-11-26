def pig_latin(texts):
    return ' '.join([text.replace(text[0],'') + text[0]+'ay' for text in texts.split()])

print(pig_latin("hello how are you"))
print(pig_latin("programming in python is fun"))
