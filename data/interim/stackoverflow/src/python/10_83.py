from datetime import datetime
import os  # Even though not used in example code.
from pprint import pprint
import re

#files = [filename for root, dirs, files in os.walk(path) for filename in files for date in dateList if filename.endswith(date+".log")]
files = [
    '[EQUIP-4].02.05.2019.log',
    '[EQUIP-2].01.05.2019.log',
    '[EQUIP-1].30.04.2019.log',
    '[EQUIP-3].29.04.2019.log',
    '[EQUIP-1].01.05.2019.log',
    '[EQUIP-5].30.04.2019.log',
    '[EQUIP-1].29.04.2019.log',
    '[EQUIP-5].30.04.2019.log',
    '[EQUIP-3].30.04.2019.log',
    '[EQUIP-1].29.04.2019.log',
    '[EQUIP-2].02.05.2019.log',
]

def get_date(filename):
    match = re.search(r".+].(\d{2}.\d{2}.\d{4})",filename)
    date_str = match.group(1)
    return datetime.strptime(date_str, '%d.%m.%Y')

files.sort(key=get_date)

pprint(files)
