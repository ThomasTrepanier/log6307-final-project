urls = ["www.annauniv.edu", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

def func(x):
  x = x.split('.')[-1]
  print(x)
  if x == 'edu':
    return 'e'
  elif x == 'com':
    return 'm'
  elif x == 'org':
    return 'o'
  else:
    return 'z'

print(sorted(urls, key=func))
