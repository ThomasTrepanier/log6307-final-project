def sal_of_seawater(l): 
        res = (-0.0222*l)+34
        return res

l = 45

print("A latitude of", l, "equals a salinity value of", sal_of_seawater(l))
