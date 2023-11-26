counter = 10
def GetInput():
    names = []
    percentage = []
    for i in range(counter):
        names.append(input("Please enter the student's name: "))
        valid = False
        while not(valid):      
            try:
                percent = int(input("Please enter the student's score between 0 and 100%: "))
                if percent >= 0 and percent <= 100:
                    percentage.append(percent)
                    valid = True
                    break
                else:
                    continue
            except ValueError:
                print("\nEnter valid marks!!!")
                continue
            valid = True

    return names, percentage

students, marks = GetInput()

