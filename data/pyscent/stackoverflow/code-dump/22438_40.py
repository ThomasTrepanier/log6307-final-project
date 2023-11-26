import time
def countdown(i):
  counter = i
  while True:
    if (counter == i):
      counter = 0
    print(counter)
    counter = counter + 1
    time.sleep(1)

countdown(30)
