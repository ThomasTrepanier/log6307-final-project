def calculator():
    age = input("Input dog years: ")
    try:
        d_age = float(age)
        ageDict = {1: 15, 2: 12, 3: 9.3, 4: 8, 5: 7.2}
        if d_age in ageDict:
            print(round(d_age*ageDict[d_age],2))
        else:
            print(round(5*7.2+(d_age - 5)*7,2))
    except ValueError:
        print(age,"is an invalid age")

calculator()
