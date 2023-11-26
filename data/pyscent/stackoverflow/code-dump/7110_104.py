def containedin(a,b):
    for j in range(len(b)-len(a)+1):
        if a==b[j:j+len(a)]:
            return True
    return False

print(containedin([2, 3, 4],[1, 2, 3, 4, 5]))
print(containedin([2, 3, 4],[1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(containedin([2, 3, 4],[5, 4, 3, 2, 1]))
print(containedin([2, 2, 2],[1, 2, 3, 4, 5]))
print(containedin([2, 2, 2],[1, 1, 1, 2, 2, 2, 3, 3, 3]))
