def count_letters(text):
  result = {}
  for letter in text:
    #check if it alphabet or something else
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      result[letter.lower()]=result.get(letter.lower(),0)+1
    # Add or increment the value in the dictionary
  return result
