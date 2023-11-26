from dateutil import parser
import re

s = 'ERROR 2019-02-03T23:21:20 cannot find file'
match = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', s)

#Datetime string
dt = match.group(0)

#Datetime object
dt_obj = parser.parse(dt)
print(dt_obj)
#2019-02-03 23:21:20

print(type(dt_obj))
#<class 'datetime.datetime'>
