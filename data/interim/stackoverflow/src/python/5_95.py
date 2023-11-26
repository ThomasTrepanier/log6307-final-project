def narcissistic(number):
  number_string = str(number)
  number_len = len(number_string)

  number_nar = 0
  for char in number_string:
    number_nar+= int(char) ** number_len        
  return number_nar

number = 153
number_nar = narcissistic(number)
print(number_nar)

number = 1634
number_nar = narcissistic(number)
print(number_nar)
