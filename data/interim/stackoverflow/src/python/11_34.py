import datetime

def proc(h, m):
    while True:
        currentHour = datetime.datetime.now().hour
        currentMinute = datetime.datetime.now().minute
        if currentHour == h and currentMinute == m:
            break
        # Do stuff...

# Function call.
proc(18,0)
