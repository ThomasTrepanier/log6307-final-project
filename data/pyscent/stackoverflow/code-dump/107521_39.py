import itertools
fruits = ['apple','mango','orange']
def apple():
  print("In apple")
def mango():
   print("In mango")
def orange():
   print("In orange")
funcs = {'apple':apple()}
funcs['apple']
