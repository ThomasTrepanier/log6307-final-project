def edit(nrows, filename):
    nrows +=1 #to avoid off-by-one error because dealing with lists

    outf = open(filename, 'a')

    column_1 = [1, 2, 3, 4, 5]
    column_2 = [10, 20, 30, 35, 50]
    column_3 = [20, 30, 50, 60, 100]

    last_column_1 = column_1[-1]
    list_1 = list(range(last_column_1+1, last_column_1+nrows))
    list_2 = nrows//len(column_2)*column_2 + column_2[0:nrows%len(column_2)]
    list_3 = nrows//len(column_3)*column_3 + column_3[0:nrows%len(column_3)]

    for c1, c2, c3 in zip(list_1, list_2, list_3):
        outf.write("{}, {}, {}\n".format(c1, c2, c3))

if __name__ == '__main__':
    edit(10, 'file.txt')
