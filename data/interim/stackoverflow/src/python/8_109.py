def rowCol(m,p):
    for r,row in enumerate(m):
        if p<len(row): return r,p
        p-=len(row)

r,c = rowCol(matrix,8)
value = matrix[r][c]
print(value) 
