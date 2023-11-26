import datetime

date1 = datetime.date(2010, 1, 1)
date2 = datetime.date(2015, 1, 1)

def daterange(date1, date2):
    for n in range(int(date2.year) - int(date1.year)+1):
        yield int(date1.year) + n

start_dt = date1
end_dt = date2
dat = []
for dt in daterange(start_dt, end_dt):
    dat.append(dt)
print(dat)
