def addSum(num):
    obj = {
        'name': "Home",
        'url': "/"
    }
    if num > 0: obj['data'] = num
    return obj

print(addSum(3))   # {'name': 'Home', 'url': '/', 'data': 3}
print(addSum(0))   # {'name': 'Home', 'url': '/'}
