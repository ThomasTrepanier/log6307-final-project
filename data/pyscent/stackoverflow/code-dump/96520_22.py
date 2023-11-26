def pig_latin(text):
  say = ""
  words = text.split()
  for word in words:
    word = str(word[1])+str(word[2:] + str(word[0:1]).lower() + 'ay')
    say = say + word + " "
  return say

print(pig_latin("hello how are you")) 
# Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))
 # Should be "rogrammingpay niay ythonpay siay unfay"
