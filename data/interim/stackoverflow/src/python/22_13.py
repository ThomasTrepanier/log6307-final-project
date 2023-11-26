mat = [[1, 2, 3, 5],
     [5, 6, 7, 1],
     [9, 10, 11, 8],
     [4, 7, 4, 3]]
 
def rotate_matrix(a):
    b = []
    i = len(a)-1
    while i>=0:
        if len(a) == len(a[-1]):
            for j in range(0, len(a)):
                print(j)
                if (len(b) < (j+1)):
                    b.append([a[i][j]])
                    print(b)
                else:
                    b[j].append(a[i][j])
                    print(b)
            i -= 1
        else:
            for j in range(0, len(a)+1):
                print(j)
                if (len(b) < (j+1)):
                    b.append([a[i][j]])
                    print(b)
                else:
                    b[j].append(a[i][j])
                    print(b)
            i -= 1
    return b
    
print(rotate_matrix(mat))
