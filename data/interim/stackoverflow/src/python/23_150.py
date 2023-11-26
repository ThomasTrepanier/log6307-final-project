from datetime import datetime
import re
class DateTime(object):
    dateFormat = {"%d": "dd", "%Y": "YYYY", "%a": "Day", "%A": "DAY", "%w": "ww", "%b": "Mon", "%B": "MON", "%m": "mm",
                  "%H": "HH", "%I": "II", "%p": "pp", "%M": "MM", "%S": "SS"}  # wil contain all format equivalent

    def __init__(self, date_str, format):
        self.dateobj = datetime.strptime(date_str, format)
        self.format = format

    def parse_format(self):
        output=None
        reg = re.compile("%[A-Z a-z]")
        fmts = None
        if self.format is not None:
            fmts = re.findall(reg, self.format)
        if fmts is not None:
            output = self.format
            for f in fmts:
                output = output.replace(f, DateTime.dateFormat[f])
        return output


nDate = DateTime("12 January, 2018", "%d %B, %Y")
print(nDate.parse_format())
