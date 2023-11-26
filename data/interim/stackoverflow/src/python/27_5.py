x = ['apple', 'orange', 'banana', 'kiwi']
enter = input('enter your fruit: ')

def exists():
    print('this fruit exists')

for fruit in x:
    if fruit == enter:
        exists()
        break
else:  # else must be under for and is executed if the loop has been executed completely, without interruption (break)
    print("this fruit doesn't exist")
