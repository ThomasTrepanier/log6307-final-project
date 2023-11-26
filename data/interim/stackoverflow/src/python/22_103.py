#function to ask user to input name and score
def GetInput():
    names=[]
    percentages=[]
    for counter in range(0,3):
        names.append(input("Please enter the student's name: "))

        valid = False
        while valid == False:
            percentages.append(int(input("Please enter the student's score %: ")))
            if percentages[counter] < 0 or percentages[counter] > 100:
                print("Please enter a valid % [0-100]")
            else:
                valid = True
    return names, percentages

name, mark = GetInput()
print(name,mark)
