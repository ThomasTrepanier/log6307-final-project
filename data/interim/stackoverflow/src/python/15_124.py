def defA() :
    return "yes"

flag = True

value = [defA() if flag else 'No' for x in range(4)]  #If you need to use else
value = [defA() for x in range(4) if flag]            #If there is no need for else
