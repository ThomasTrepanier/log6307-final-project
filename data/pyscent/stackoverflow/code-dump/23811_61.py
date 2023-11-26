def function(n):
   from random import randrange
   values = ['value1', 'value2']
   mydict = {"key " + str(i): values[0] for i in range(n)}
   mydict["key " + str(random.randrange(n))] = values[1]

   return mydict
