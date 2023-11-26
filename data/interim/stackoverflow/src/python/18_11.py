def check_the_first_letter_of_two_words(word):
  new_word = word.lower().split()
  if new_word[0][0] == new_word[1][0]:
    return True
  else:
    return False

word1 = 'Hello World'
word2 = 'World wide'
check_the_first_letter_of_two_words(word1)
check_the_first_letter_of_two_words(word2)
