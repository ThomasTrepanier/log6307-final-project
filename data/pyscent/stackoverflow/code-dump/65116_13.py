from datetime import date, timedelta

def date_range_list(start_date, end_date):
    # Return generator for a list datetime.date objects (inclusive) between start_date and end_date (inclusive).
    curr_date = start_date
    while curr_date <= end_date:
        yield curr_date 
        curr_date += timedelta(days=1)

start_date = date(year=2021, month=12, day=20)
stop_date = date(year=2021, month=12, day=25)
date_list = date_range_list(start_date, stop_date)

for date in date_list:
   print(date)
