import time
import datetime

start_time = datetime.datetime(year=2022, month=4, day=5, hour=1, minute=00, second=00)
relativedelta = datetime.timedelta(hours=1)
iteration_time = datetime.timedelta(minutes=5)

end_time = start_time + relativedelta
last_run = None


def func():
    print("this is python")


while True:
    current_time = datetime.datetime.now()
    if start_time <= current_time <= end_time:
        if last_run:
            if current_time >= last_run + iteration_time:
                func()
                last_run = current_time
        else:
            last_run = current_time
    elif current_time > end_time:
        break

    time.sleep(1)
