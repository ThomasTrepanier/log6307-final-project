def fill_in_numbers(lst):
  new_list = []
  for i in range(len(lst)):
    new_list.append(lst[i])
    if i+1 < len(lst):
      [new_list.append(k) for k in range(lst[i]+1, lst[i+1])]
  return new_list


print(fill_in_numbers([12,15,19])) # --- Output --->>> [12, 13, 14, 15, 16, 17, 18, 19] 
print(fill_in_numbers([ -5,0, 5])) # --- Output --->>> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
