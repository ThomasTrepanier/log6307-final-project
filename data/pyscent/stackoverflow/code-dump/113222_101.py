def GetInput():
    names = {}  # Needs to declare your dict
    percentages = {}  # Needs to declare your dict
    for counter in range(0, 3):
        names[counter] = input("Please enter the student's name: ")

        valid = False
        while valid == False:
            percentages[counter] = int(input("Please enter the student's score %: "))
            if percentages[counter] < 0 or percentages[counter] > 100:
                print("Please enter a valid % [0-100]")
            else:
                valid = True
    return names, percentages  # Return outside of for loop.

name, mark = GetInput()
print(name)
print(mark)
