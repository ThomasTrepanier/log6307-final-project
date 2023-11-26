sOdd = "The cat jumped over the moon very quickly."
sEven = "The cat jumped over the moon very quickly now."

def split_on_delim_mid(s, delim=" "):
  delim_indexes = [
      x[0] for x in enumerate(s) if x[1]==delim
  ] # [3, 7, 14, 19, 23, 28, 33]

  # Select the correct number from delim_indexes
  middle = len(delim_indexes)/2
  if middle % 2 == 0:
    middle_index = middle
  else:
    middle_index = (middle-.5)

  # Return the separated sentances
  sep = delim_indexes[int(middle_index)]
  return s[:sep], s[sep:]

split_on_delim_mid(sOdd) # ('The cat jumped over', ' the moon very quickly.')
split_on_delim_mid(sEven) # ('The cat jumped over the', ' moon very quickly now.')
