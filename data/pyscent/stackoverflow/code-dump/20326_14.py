def powers_of_two():
    i = 1
    while True:
        yield i
        i *= 2


for i in powers_of_two():
    ...
    if some_condition:
        break
    
