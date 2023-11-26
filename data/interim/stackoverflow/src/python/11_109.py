l = [
   '/api/users/*',
   '/api/account/'
]

paths = [
'/api/users/add/',
'/api/users/edit/1',
'/api/users/',
'/api/account/view/1',
'/api/account/'
]

def checkPath(path):
        if path in l:
            return True
        else:
            return False

for i in range(0,len(paths)):
    print(checkPath(paths[i]))
