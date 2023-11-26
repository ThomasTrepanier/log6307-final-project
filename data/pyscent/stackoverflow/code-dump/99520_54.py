def pig_latin(text):
  say = []
  # Separate the text into words
  words = text.split(" ")
  for word in words:
    # Create the pig latin word and add it to the list
    say.append(word[1:]+word[0]+'ay')
    # Turn the list back into a phrase
  return " ".join(x for x in say)
