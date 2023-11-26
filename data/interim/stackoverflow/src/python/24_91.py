def years_of_age():
    from datetime import date, datetime
    dob = input("Please enter your DOB as mm-dd-yyyy: ")

    #time delta in days
    val = date.today().toordinal() - datetime.strptime(dob, "%m-%d-%Y").toordinal()

    # this is just so you can confirm, comment out the following 4 lines
    print("months {}, years {}".format(\
                                       int(datetime.fromordinal(val).strftime("%m")),\
                                       int(datetime.fromordinal(val).strftime("%Y"))\
                                      ))

    # conditional return based on the months figure
    if int(datetime.fromordinal(val).strftime("%m")) >=6:
        return int(datetime.fromordinal(val).strftime("%Y")) + 1
    else:
        return int(datetime.fromordinal(val).strftime("%Y"))
