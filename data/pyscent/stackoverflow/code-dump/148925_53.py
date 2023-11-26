from datetime import datetime, timedelta

x = datetime(2020, 1, 2) # this is Thursday and week 1 in ISO calendar; should be 1 in custom calendar w/ week starting Thu
y = datetime(2020, 1, 3) # this is Friday and week 1 in ISO calendar; should be 2 in custom calendar
print(x)
print(y)

def weeknum(dt):
    return dt.isocalendar()[1]

def myweeknum(dt):
    offsetdt = dt + timedelta(days=3);  # you add 3 days to Mon to get to Thu 
    return weeknum(offsetdt);

print(weeknum(x));
print(myweeknum(x));

print(weeknum(y));
print(myweeknum(y));
