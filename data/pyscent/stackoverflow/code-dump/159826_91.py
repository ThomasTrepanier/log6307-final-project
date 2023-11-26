class MyException(Exception):
    pass


try:
    value = dict['h']
except KeyError:
    raise MyException('my message')
