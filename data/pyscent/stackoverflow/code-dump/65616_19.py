from datetime import date, timedelta

#-- the actual method --#
def get_start_to_end(start_date, end_date):
    date_list = []
    for i in range(0, (end_date - start_date).days + 1):
        date_list.append(  str(start_date + timedelta(days=i))  ) #<-- here
    return date_list
#-- end of the actual method --#

# -- demonstrating it --#
sd = date(2022,8,12)
ed = date(2022,11,17)
dates = get_start_to_end(sd, ed)

for d in dates:
    print(d)

#-- You can just append the date object, the default string (iso)
#-- or use strftime for a different format
#-- (start_date + timedelta(days=i)) <-- date object
#-- str(start_date + timedelta(days=i))  <-- default string
#-- (start_date + timedelta(days=i)).strftime("%b %d, %Y") <-- other string format
