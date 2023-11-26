import re
def myfunction(bigstring):
    return  re.findall(r'[\w\.-]+@[\w\.-]+', bigstring)

emails = ['John Kennedy <jk123@gmail.com> or <johnk123@hotmail.com>','Adam Hartley <ah123@yahoo.com>','Ben Saunders <benji@live.co.uk>']


output = []
for emailstring in emails:
    output.append((myfunction(emailstring)))
print(output)
