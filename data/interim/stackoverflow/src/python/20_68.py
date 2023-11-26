def pig_latin(text):
  say = ""
  words = text.split()
  for word in words:
    word=word[1:] + word[0] + "ay" + " "
    say +=word
  return say
        
print(pig_latin("hello how are you"))
