#!/usr/bin/env python3

fruits = ['apple','mango','orange']

def apple():
  print("In apple")
def mango():
   print("In mango")
def orange():
   print("In orange")

for func in fruits:
    exec(func + '()')  
