def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.lower():
    # Check if the letter needs to be counted or not
    if(letter.isalpha()):
      result[letter] = result.get(letter,0)+1
    # Add or increment the value in the dictionary
    
  return result
