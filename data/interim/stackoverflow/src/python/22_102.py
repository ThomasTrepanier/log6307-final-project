def GetInput():
    students = {}
    for _ in range(0, 3):
        student_name = input("Please enter the student's name: ")
        valid = False
        while not valid:
            student_percentages = int(input("Please enter the student's score %: "))
            if student_percentages < 0 or student_percentages > 100:
                print("Please enter a valid % [0-100]")
                continue
            valid = True
            students[student_name] = student_percentages
    return students


students = GetInput()
print(students)
