def num_characters(string):
  total = 0
  for character in string:
    total += 1
  return total

original_string = "The quick brown rhino jumped over the extremely lazy fox."
print(f"The numbers of characters in the original string using `len` is {len(original_string)}.")
print(f"The numbers of characters in the original string using `num_characters` is {num_characters(original_string)}.")
