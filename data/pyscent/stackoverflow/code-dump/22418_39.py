import time
start_time = time.time()
def countdown():
  global countDown
  countDown = int(time.time() - start_time)
  return countDown % 30

print("You have " + str(30 - countdown()) + " time")
