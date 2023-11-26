import datetime
import getpass
import threading
import time

def save_datetime(file='date.txt', user=getpass.getuser()):
    with open(file, 'a+') as f:
        f.write('register: ' + user + '\t' + str(datetime.datetime.now().time()) + '\n')

def threadingtime_every_sec(sec=60):
    def loop():
        while True:
            save_datetime()
            time.sleep(sec)
    threading.Thread(target=loop).start()

if __name__ == '__main__':
    threadingtime_every_sec(1)
