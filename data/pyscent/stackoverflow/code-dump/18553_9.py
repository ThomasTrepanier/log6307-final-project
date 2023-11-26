list1 = ['list4','this1', 'he5re', 'my3','is2']

def mySort(string):
    if any(char.isdigit() for char in string): #Check if theres a number in the string
        return [float(char) for char in string if char.isdigit()][0] #Return list of numbers, and return the first one (we are expecting only one number in the string)

list1.sort(key = mySort)

print(list1)
