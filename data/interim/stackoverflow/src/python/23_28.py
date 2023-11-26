import datetime
import time


def repeat_between(
        start_dt,
        stop_dt,
        interval_td,
        func,
        func_args=None,
        func_kws=None,
        collect_results=True,
        throttling_s=1):
    # ensure valid `func_args` and `func_kws`
    func_args = () if func_args is None else tuple(func_args)
    func_kws = {} if func_kws is None else dict(func_kws)
    # initialize current datetime and last run
    curr_dt = datetime.datetime.now()
    last_run = None
    # ensure the start datetime is:
    # - before the stop datetime
    # - after the current datetime
    if stop_dt < start_dt < curr_dt:
        return
    else:
        # collect results here
        result = []
    # wait until reaching the start datetime
    wait_td = (start_dt - curr_dt)
    time.sleep(wait_td.total_seconds())
    # loop until current datetime exceeds the stop datetime
    while curr_dt <= stop_dt:
        # if current time is
        # - past the start datetime
        # - near an interval timedelta
        if curr_dt >= start_dt and \
                (not last_run or curr_dt >= last_run + interval_td):
            curr_result = func(*func_args, **func_kws)
            if collect_results:
                result.append(curr.result)
            last_run = curr_dt
        # wait some time before checking again
        if throttling_s > 0:
            time.sleep(throttling_s)
        # update current time
        curr_dt = datetime.datetime.now()
