import random

def function(n):
   mydict = dict.fromkeys(("key "+ str(i) for i in range(n)), 'value1')
   mydict["key "+ str(random.randrange(n))] = 'value2'  # Change one value.
   return mydict

print(function(3))  # -> {'key 0': 'value1', 'key 1': 'value1', 'key 2': 'value2'}
print(function(5))  # -> {'key 0': 'value2', 'key 1': 'value1', 'key 2': 'value1', 'key 3': 'value1', 'key 4': 'value1'}
