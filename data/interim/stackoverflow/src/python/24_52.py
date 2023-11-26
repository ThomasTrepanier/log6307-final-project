import datetime

def minutes_of_year(dt):
    return seconds_of_year(dt) // 60

def hours_of_year(dt):
    return minutes_of_year(dt) // 60

def seconds_of_year(dt):
    dt0 = datetime.datetime(dt.year, 1, 1, tzinfo=dt.tzinfo)
    delta = dt-dt0
    return int(delta.total_seconds())
