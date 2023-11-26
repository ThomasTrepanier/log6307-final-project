from dateutil.parser import parse
from functools import wraps

def parse_wrapper(function):
    @wraps(function)
    def wrapper(*args):
        return {'datetime': function(*args), 'args': args}
    return wrapper

wrapped_parse = parse_wrapper(parse)
x = wrapped_parse("2014-01-01 00:12:12")
# {'datetime': datetime.datetime(2014, 1, 1, 0, 12, 12),
#  'args': ('2014-01-01 00:12:12',)}
