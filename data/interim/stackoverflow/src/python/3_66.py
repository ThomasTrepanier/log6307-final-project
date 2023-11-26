array  = [[0, 1],[2, 3],[4, 5]] 

def get_index(array):
  i = 0

  for element in array:
    if(element[0]==2):
      break
    i+=1

  return i 

print(str(get_index(array)))
