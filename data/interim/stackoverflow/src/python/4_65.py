import datetime

def week_to_dates():
    date = datetime.date.today()
    week = date.strftime("%V")

    candidates = [date - datetime.timedelta(days=k) for k in range(14, 0, -1)] + \
                 [date] + \
                 [date + datetime.timedelta(days=k) for k in range(1, 15)]
    return [candidate.strftime('%Y-%m-%d') for candidate in candidates if candidate.strftime("%V") == week]
