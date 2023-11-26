def convert_to_proper_type(value):
    if value.isalpha():
        value = str(value)
    elif value.isdigit():
        value = int(value)
    else:
        value = float(value)
    return value

result = [('Books', '10.000'),('Pen', '10'),('test', 'a')]
newresult = []

for (value_one, value_two) in result:
    # If all chars in both are alphabets
    value_one = convert_to_proper_type(value_one)
    value_two = convert_to_proper_type(value_two)
    newresult.append((value_one, value_two))

print(newresult)
# [('Books', 10.0), ('Pen', 10), ('test', 'a')]
