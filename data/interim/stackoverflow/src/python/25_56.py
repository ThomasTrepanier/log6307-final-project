def alldays(year, whichDayYouWant):
    d = date(year, 1, 1)
    d += timedelta(days = (weeknum(whichDayYouWant) - d.weekday()) % 7)
    while d.year == year:
        yield d
        d += timedelta(days = 7)
