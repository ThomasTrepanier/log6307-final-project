import time

class countdown():
    def start(self):
        self.t = time.time()
    def remaining(self):
        return 30 - int(time.time()-self.t)


timer = countdown()
timer.start()
while True:
    print(30 - countdown(), "seconds remaining") #Still time left code
    if timer.remaining() <= 0:
        pass #30 seconds over code
        timer.reset() #Starts timer again
