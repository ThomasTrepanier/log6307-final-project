def to_date(date):
    return datetime.strptime(date, '%Y-%m-%d').toordinal()

for g in consecutive_groups(dates, to_date):
    print(list(g))
