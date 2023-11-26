def fibonacci_numbers(format_width):
  how_many_numbers = int(input("\nHow many Fibbonacci numbers you want print: "))
  i = 0
  res = [0, 1]
  while i < how_many_numbers:
      res.append(sum(res[-2:]))
      # Here we specify alignment to right with certain width 
      # which is >= number of digits of the largest integer in your sequence.:
      print("{}. {:>{width}}".format(i + 1, res[i], width=format_width)) 
      i += 1


fibonacci_numbers(30)
