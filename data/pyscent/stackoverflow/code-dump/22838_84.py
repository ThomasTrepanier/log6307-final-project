def my_function(str_array):
    return [re.findall(r'[\w\.-]+@[\w\.-]+', s) for s in str_array]

emails = ['John Kennedy <jk123@gmail.com> or <johnk123@hotmail.com>','Adam Hartley <ah123@yahoo.com>','Ben Saunders <benji@live.co.uk>']

my_function(emails)
