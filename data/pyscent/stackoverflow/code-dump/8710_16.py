# fname : file name
# x : number of characters or length
def delete_lines(fname = 'test.txt', x = 8):
    with open(fname, "r") as f:
        lines = f.readlines()
    with open(fname, "w") as f:
        for line in lines:
            if len(line) <= x:            
                f.write(line)

delete_lines()
