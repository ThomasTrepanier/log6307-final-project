def pig_latin(text):
    say = "ay"
    # Separate the text into words
    words = text.split()
    newtext = []
    # Create the pig latin word and add it to the list
    for newword in words:
        newlist = newword[1:] + newword[0] + say
        newtext.append(newlist)
    return " ".join(newtext)
