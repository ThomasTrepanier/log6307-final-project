import re
def to_snake(s):
  return re.sub('([A-Z]\w+$)', '_\\1', s).lower()

def t_dict(d):
   if isinstance(d, list):
      return [t_dict(i) if isinstance(i, (dict, list)) else i for i in d]
   return {to_snake(a):t_dict(b) if isinstance(b, (dict, list)) else b for a, b in d.items()}
