def daterange(date1, date2):
    for n in range(int(date2.year) - int(date1.year)+1):
        yield int(date1.year) + n

lst = [item for item in daterange(start_dt, end_dt)]
