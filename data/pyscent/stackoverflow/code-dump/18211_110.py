def checkPath(path):
        if path in l_new:
            return True
        else:
            return False

# strip the asterick
l_new = [s.strip('*') for s in l]

for i in range(0,len(paths)):
    print(checkPath(paths[i]))
