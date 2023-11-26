from datetime import datetime, timedelta
from datetime import date


def date_bwn_two_dates(start_date, end_date):
    date_list = [] # The list where we want to store
    for i in range(int((end_date-start_date).days)+1): # Iterate between the range of dates
        year = (start_date+timedelta(i)).strftime("%Y") # Get the Year
        month = (start_date+timedelta(i)).strftime("%m") # Get the month
        date_a = (start_date+timedelta(i)).strftime("%d") # Get the day
        date_list.append([year, month, date_a]) # Append the Objects accquired
    return date_list # return the list


for i in date_bwn_two_dates(date(2020, 12, 1), date(2021, 12, 1)):
    print(i)
