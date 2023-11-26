x = ['apple','orange','banana','kiwi']

enter = str(input('enter your fruit: '))

def exists():
  print('this fruit exists')

enter = enter.lower()

fruitExist = False

for fruit in x:
   if fruit.lower() == enter:
     fruitExist = True
     break

if fruitExist :
    exists()
else:
   print("this fruit doesn't exist")
