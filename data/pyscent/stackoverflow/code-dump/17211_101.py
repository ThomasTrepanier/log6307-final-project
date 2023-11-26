def string_skip_2(string):
   string = list(string)
   new_string = ''
   for i in range(len(string)):
       if int(list(enumerate(string))[i][0]) % 2 == 0:
           new_string += list(enumerate(string))[i][1]
   return new_string
