from datetime import datetime, timedelta
from enum import IntEnum

WEEKDAY = IntEnum('WEEKDAY', 'MON TUE WED THU FRI SAT SUN', start=1)

def get_week_number(start, date):
    year_start = datetime(date.year, 1, 1) - timedelta(days=(datetime(date.year, 1, 1).isoweekday() - start) % 7)
    return date.year, (date-year_start).days // 7 + 1, (date-year_start).days % 7 + 1

if __name__ == '__main__':
    # usage:
    print(get_week_number(WEEKDAY.FRI, datetime(2018, 12, 19)))
