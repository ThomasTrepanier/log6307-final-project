def calculator():
    # Get dog age
    age = input("Input dog years: ")
    try:
    # Cast to float
        d_age = float(age)
        if (d_age> 5):
            human_age = (d_age-5)*7+5*7.2
            print("The given dog age",str(d_age),"is", str(human_age), "in human years")
        elif (d_age>4):
                human_age = d_age*7.2
                print("The given dog age",str(d_age),"is",str(human_age),"in human years")
        elif (d_age>3):
                human_age = d_age*8
                print("The given dog age",str(d_age),"is",str(human_age),"in human years")
        elif (d_age>2):
                human_age = d_age*9.3
                print("The given dog age",str(d_age),"is",round(human_age,2),"in human years")
        elif (d_age>1):
                human_age = d_age*12
                print("The given dog age",str(d_age),"is",str(human_age),"in human years")
        elif (d_age>0):
                human_age = d_age*15
                print("The given dog age",str(d_age),"is",str(human_age),"in human years")
        elif (d_age<0 or d_age==0):
                print(d_age, "is a negative number or zero. Age can not be that.")
    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
        
calculator()
