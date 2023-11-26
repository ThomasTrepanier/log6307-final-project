def convert(value, decimals):
     value = str(value) # convert value to string-type for indexing
     d1 = value[:-decimals] # d1 comes before the decimal
     d2 = value[-decimals:] # d2 comes after the decimal
     output = f"{d1}.{d2}" # join d1 and d2 with . using f-string
     return output

print(convert(11098, 2))

110.98
