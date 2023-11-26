def myfunction(bigstring):
    #str = ' '.join(bigstring)
    #my_string = str
    str1 = re.findall(r'[\w\.-]+@[\w\.-]+', bigstring)
    return str1

import re
output=[]
emails = ['John Kennedy <jk123@gmail.com> or <johnk123@hotmail.com>','Adam Hartley <ah123@yahoo.com>','Ben Saunders <benji@live.co.uk>']
for item in emails:
    output.append(myfunction(item))

print(output)
