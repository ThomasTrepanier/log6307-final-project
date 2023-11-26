def specialRound(num):
    #check if has decimals
    intForm = int(num)
    if(num==intForm):
        return intForm
    TDNumber = round(num,2) #Two decimals
    ODNumber = round(num,1) #One decimal
    if(TDNumber>ODNumber):
        return TDNumber
    return ODNumber

print(specialRound(3.1415))
print(specialRound(3.10))
print(specialRound(3))
