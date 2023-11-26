import multiprocessing as mp
import time
import datetime
import sys
import signal
import os

def process(hr, minute):
    while True:
        d = datetime.datetime.now()
        if d.hour == hr and d.minute == minute:
            os.kill(os.getppid(), signal.SIGTERM)
            sys.exit()
        else:
            time.sleep(25)


p = mp.Process(target=process, args=(18, 0))
p.start()

# your program here ...
