
def GetInput():
    records = dict()
    for i in range(counter):
        name = input("Please enter the student's name: ")
        valid = False
        while not(valid):      
            try:
                percent = int(input("Please enter the student's score between 0 and 100%: "))
                if percent >= 0 and percent <= 100:
                    #percentage.append(percent)
                    valid = True
                    break
                else:
                    continue
            except ValueError:
                print("\nEnter valid marks!!!")
                continue
            valid = True
        records[name] = percent
    return records

record = GetInput()
