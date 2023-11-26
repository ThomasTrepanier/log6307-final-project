import random
from students.models import students

pars = students.objects.all()

def groupp (x, y):
    res = random.sample(x, y)
    while len(set([u.first_language for u in res])) < y:
        res = random.sample(x, y)
    return res
