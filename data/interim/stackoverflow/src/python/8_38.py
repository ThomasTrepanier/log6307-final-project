from time import time

def do_something():
    pass

def get_time(start_time):
    # returns how much time did it pass from event that started at start_time
    return time() - start_time

def countdown(countDown):
    start_time = time()
    # this is counter that attains consecutive values [0, 1, ..., countDown]
    current_count = 0
    while current_count < countDown:
        print(countDown - current_count, end=' ')
        while get_time(start_time) - current_count < 1:
            do_something()
            #warning: if do_something takes significant anount of
            #time forthcoming print won't be correct
        current_count += 1
    print(countDown - current_count, end=' ')
    return current_count

countdown(7)
countdown(5)
