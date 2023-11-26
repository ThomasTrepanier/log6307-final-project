import datetime

def get_most_common_days(year, month):
    days = []
    for daynum in range(29, 32):
        try:
            days.append(datetime.date(year, month, daynum).strftime('%A'))
        except ValueError:
            break
    return days

print(get_most_common_days(2020, 8))
