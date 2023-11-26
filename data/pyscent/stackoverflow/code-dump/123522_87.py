def rotate_matrix(a):
    b = []
    i = len(a)-1
    while i>=0:
        for j in range(0, len(a)):
            if (len(b) < (j+1)):
                b.append([a[i][j]])
            else:
                b[j].append(a[i][j])
        i -= 1
    return b
