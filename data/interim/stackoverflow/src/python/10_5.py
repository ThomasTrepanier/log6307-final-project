def func(start,end, step):
    if(start >= end):
        return 0

    return start + func(start + step, end, step)
