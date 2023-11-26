l = ['ones', 'twos', 'threes']
wanted = 'three'

def run():
    for s in l:
        if (s.startswith(wanted)):
            return s

print(run())
