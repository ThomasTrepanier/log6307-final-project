import datetime

class Minutes:
  d = datetime.datetime.now()
  def __init__(self, _str, _year = None):
    self._val = _str
    d = datetime.datetime.now()
    self.year = _year if _year is not None else '-'.join(str(getattr(d, i)) for i in ['year', 'month', 'day'])
  @property
  def to_date(self):
    return datetime.datetime(*map(int, self.year.split('-')), *map(int, str(self).split(':')))
  def __str__(self):
    _h, _m, _s = map(int, self._val.split(':'))
    h, m, s = 0 if _h else _h, _m+(_h*60) if _h else _m, _s
    return f'{self.year} '+':'.join(str(i).zfill(2) for i in [h, m, s])
  def __repr__(self):
    return str(self)

x = ['59:55:00', '59:55:00', '59:58:00', '1:00:02', '1:00:05', '1:01:26']
new_x = [Minutes(i, '1900-01-01') for i in x]    
