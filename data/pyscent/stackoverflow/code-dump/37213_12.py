my_dict = {'Stock_A': (100, 0.5), 'Stock B': (20, 0.9), 'Stock C': (40, 0.75), 'Stock D': (45, 0.3)}
new_dict = {} # Dictionary in which the TRUE conditions are stores


# Function which makes the comparison
def comp(Val1,Val2):
    Values = [30,0.6]
    if Val1 > Values[0] and Val2 < Values[1]:
        return True,(Val1,Val2)
    else:
        return False,None

# Creates the new dictionary   
for key in my_dict:
    Res = comp(my_dict[key][0],my_dict[key][1])
    if Res[0]:
        new_dict[key] = Res[1]


print(new_dict)







{'Stock_A': (100, 0.5), 'Stock D': (45, 0.3)}
