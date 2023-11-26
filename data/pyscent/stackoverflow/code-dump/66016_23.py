from datetime import date, timedelta

def timer():
    global datelist
    sdate = date(2022, 5, 1)
    edate = date(2022, 6, 1)

    delta = edate - sdate       
    datetimes = []
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        datetimes.append(day)


    def formatting():
        global converted
        converted = pd.to_datetime(datetimes)
        return converted

    datelist = converted.strftime("%Y-%m-%d").tolist()

    formatting()
