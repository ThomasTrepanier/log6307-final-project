def get_final_lines(fin):
    buf = []
    for line in fin:
        if line.startswith('STARTINGWORK'):
            buf = []
        else:
            buf.append(line)

    yield from buf


if __name__ == '__main__':
    with open('some_file.txt') as fin:
        for line in get_final_lines(fin):
            print(line.rstrip())
