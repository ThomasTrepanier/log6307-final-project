def repeat(s, number):
    result = ''
    for _ in range(0, number):
         result += s
    return result

print(repeat("Hi", 3))
