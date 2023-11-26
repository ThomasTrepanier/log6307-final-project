from fnmatch import fnmatch

def listglob(path, patterns):
    return any(fnmatch(path, pat) for pat in patterns)

for path in paths:
    print(path, listglob(path, l))
