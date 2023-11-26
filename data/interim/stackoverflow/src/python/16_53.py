def octal_to_string(octal):
    permission = ["---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx"]
    result = ""
    # Iterate over each of the digits in octal
    for ___ in [int(n) for n in str(octal)]:
        result += permission[___]
    return result

print(octal_to_string(755)) 
print(octal_to_string(644)) 
print(octal_to_string(750)) 
print(octal_to_string(600)) 
