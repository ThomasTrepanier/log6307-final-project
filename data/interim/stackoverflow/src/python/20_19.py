def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  last = words[-1]
  for word in words:
    if word == last:
        say += word[1:]+word[0]+"ay"
    else:
         say += word[1:]+word[0]+"ay "
  return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
