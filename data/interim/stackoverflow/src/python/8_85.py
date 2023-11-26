import re

emails = ['John Kennedy <jk123@gmail.com> or <johnk123@hotmail.com>','Adam Hartley <ah123@yahoo.com>','Ben Saunders <benji@live.co.uk>']
def myfunction(bigstring):
    result = []
    for s in bigstring:
        result.append(re.findall(r'[\w.-]+@[\w.-]+', s))
    return result

print(myfunction(emails))
# => [['jk123@gmail.com', 'johnk123@hotmail.com'], ['ah123@yahoo.com'], ['benji@live.co.uk']]
