a = ['hello 123', 'pumpkin 542', 'muffin 342']

def get_important_part(string):
    return int(string.split()[1])

print(sorted(a, key=get_important_part))
