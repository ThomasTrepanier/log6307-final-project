fileinput = """
 Company         Adress      Employees   Phone Nr.
Venganese| Big street, Egypt|   52     |2214124112
Monyess  | One street, Malta|   89     |2215521575

"""

def findbynumber(data, number):
    lines = [line
             for line in data.split("\n") if line
             for parts in [line.split("|")] if len(parts) == 4 and parts[3] == number]
    return lines

print(findbynumber(fileinput, "2215521575"))
