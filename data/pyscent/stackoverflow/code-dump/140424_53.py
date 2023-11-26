import datetime

class MyDateTime(datetime.datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.datetime.__new__(cls, *args, **kwargs)

    def minutes_of_year(self):
        return self.seconds_of_year() // 60

    def hours_of_year(self):
        return self.minutes_of_year() // 60

    def seconds_of_year(self):
        dt0 = datetime.datetime(self.year, 1, 1, tzinfo=self.tzinfo)
        delta = self-dt0
        return int(delta.total_seconds())

# create and use like a normal datetime object
dt = MyDateTime.now()
# properties and functions of datetime still available, of course.
print(dt.day)
# ... and new methods:
print(dt.hours_of_year())
