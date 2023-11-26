import random
def my_function(n):
    mydict = {}
    value2_index = random.randint(0, n-1)
    for i in range(n):
        key = "key " + str(i)
        if i == value2_index:
            value = ['value2']
        else:
            value = ['value1']
        mydict.update({key: value})
    return mydict
thing = my_function(5)
print(thing)
