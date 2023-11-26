def count_letters(text):
  result = {}
  # Go through each letter in the text
  text_lower=text.lower()
  # Go through each letter in the text
  for letter in text_lower:
    # Check if the letter needs to be counted or not
    if letter.isalpha() and letter != " ":
      if letter not in result:
        result[letter] = 0  
    # Add or increment the value in the dictionary
      result[letter] += 1
  return result
