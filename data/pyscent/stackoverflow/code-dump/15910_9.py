import ast
from pprint import pprint

def parse_dict_multikey(s):
    p = ast.parse(s)
    exp_dict = p.body[0].value
    keys = list(map(ast.literal_eval, exp_dict.keys))
    values = list(map(ast.literal_eval, exp_dict.values))
    d = {}
    for k, v in zip(keys, values):
        d.setdefault(k, []).append(v)
    return d

s = ('{"Date": "Fri, 19 Apr 2019 00:54:46 GMT",'
     ' "Vary": "Host,Accept-Encoding",'
     ' "Key-Word": "00a",'
     ' "Cache-Control": "private",'
     ' "Key-Word": "xn"}')
pprint(parse_dict_multikey(s))
# {'Cache-Control': ['private'],
#  'Date': ['Fri, 19 Apr 2019 00:54:46 GMT'],
#  'Key-Word': ['00a', 'xn'],
#  'Vary': ['Host,Accept-Encoding']}
