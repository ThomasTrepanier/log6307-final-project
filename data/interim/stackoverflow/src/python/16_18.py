def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    
    for num in [int(n) for n in str(octal)]:
        
        for value, letter in value_letters:
            if num >= value:       #checks if num not exceeds value of value_letters
                result += letter   #adds coherent letter to result 
                num -= value       #substracts for new value to check next permission
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
