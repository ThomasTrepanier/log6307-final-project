languages = ['thai01', 'thai02', 'thai03', 'jap01', 'jap02', 'jap03']

thai = []

def filter_str(lang):
    if 'tha' in lang:
        return True
    else:
        return False

for x in languages:
    if filter_str(x):
        thai.append(x)

print(thai)
# ['thai01', 'thai02', 'thai03']
