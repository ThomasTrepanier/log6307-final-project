import datetime

dates = [datetime.date(2018, 7, 2),
         datetime.date(2018, 7, 5),
         ...,
         datetime.date(2019, 3, 30),
         datetime.date(2019, 4, 8)]


def are_consecutive(d1, d2):
    return d2-d1 == datetime.timedelta(1)

filtered_out = set()
consecutive = set()
for i,d in enumerate(sorted(dates)):
    try:
        d1,d2 = dates[i:i+2]
    except:
        break
    if are_consecutive(d1, d2):
        consecutive.add(d1)
        consecutive.add(d2)
    else:
        if len(consecutive) >= 3:
            for date in consecutive:
                filtered_out.add(date)
        consecutive = set()

selected = [d for d in dates if d not in filtered_out]
