from threading import Event
from time import sleep
import keyboard

hotkey = 'k'

running = Event()
running.set()  # at the start, it is running

def handle_key_event(event):
    if event.event_type == 'down':
        # toggle value of 'running'
        if running.is_set():
            running.clear()
        else:
            running.set()

# make it so that handle_key_event is called when k is pressed; this will 
# be in a separate thread from the main execution
keyboard.hook_key(hotkey, handle_key_event)

while True:
    if not running.is_set():
        running.wait()  # wait until running is set
    sleep(0.1)        
    print('hello')
