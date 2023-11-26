import re
def reposition(s):
   return re.sub('\d+', '{}', s).format(*sorted(map(int, re.findall('\d+', s)), reverse=True))

vals = ['I am 5 years and 11 months old', 'I am 28 years 9 months 11 weeks and 55 days old']
result = [reposition(i) for i in vals]
