def count_letters(text):
  result = {}
  for letter in text.lower():
    if letter.isalpha():
      lettercount = text.lower().count(letter)
      result[letter] = lettercount
  return result
