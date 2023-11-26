def pig_latin(text):
  # Separate the text into words
  words = text.split()
  list1 = []
  for word in words:
    # Create the pig latin word and add it to the list
    pig_latin = word[0] + "ay"
    mod_word = word.replace(word[0],"")
    mod_word2 = mod_word + pig_latin
    list1.append(mod_word2)
    # Turn the list back into a phrase
  return " ".join(list1)
        
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

