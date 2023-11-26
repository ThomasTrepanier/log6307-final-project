import datetime
from threading import Thread, Event
import time
from typing import Callable


class TimedCalls(Thread):
    """Call function again every `interval` time duration after it's first run."""
    def __init__(self, func: Callable, interval: datetime.timedelta) -> None:
        super().__init__()
        self.func = func
        self.interval = interval
        self.stopped = Event()

    def cancel(self):
        self.stopped.set()

    def run(self):
        next_call = time.time()
        while not self.stopped.is_set():
            self.func()  # Target activity.
            next_call = next_call + self.interval
            # Block until beginning of next interval (unless canceled).
            self.stopped.wait(next_call - time.time())


def my_function():
    print(f"this is python: {time.strftime('%H:%M:%S', time.localtime())}")

# Start test a few secs from now.
start_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
run_time = datetime.timedelta(minutes=2)  # How long to iterate function.
end_time = start_time + run_time

assert start_time > datetime.datetime.now(), 'Start time must be in future'

timed_calls = TimedCalls(my_function, 10)  # Thread to call function every 10 secs.

print(f'waiting until {start_time.strftime("%H:%M:%S")} to begin...')
wait_time = start_time - datetime.datetime.now()
time.sleep(wait_time.total_seconds())

print('starting')
timed_calls.start()  # Start thread.
while datetime.datetime.now() < end_time:
    time.sleep(1)  # Twiddle thumbs while waiting.
print('done')
timed_calls.cancel()

