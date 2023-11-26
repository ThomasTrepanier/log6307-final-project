def pig_latin(text):
  say = ""
  words = text.split()
  for word in words:
    pig_word = word[1:] + word[0] + "ay "
    say += pig_word
  return say
        
print(pig_latin("hello how are you")) # "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # "rogrammingpay niay ythonpay siay unfay"
