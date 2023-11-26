import re
def new_path(s):
  _, a, b, f_type = re.findall('[a-zA-Z0-9]+', s)
  new_b = '_'.join(b[i:i+2] for i in range(0, len(b), 2))
  return f'{a[:4]}-{a[4:6]}-{a[6:]}_{new_b}.{f_type}'

print(new_path('IMG_20190401_235959.jpg'))
