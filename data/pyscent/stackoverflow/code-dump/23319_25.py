def main():
    file = open('file.txt', 'r')
    students = {}
    for line in file:
        fields = line.split(" ")
        fields[2] = fields[2].replace("\n", "")
        students[fields[1]] = [fields[0], fields[2]]

    print(students)
main()
