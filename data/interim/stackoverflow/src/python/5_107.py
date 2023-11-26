def cleanText(val):
    result = []
    for i in val:
        if not result:
            result.append(i)
        else:
            if result[-1] != i:
                result.append(i)
    return "".join(result)

s = ['hiiii how are you??', 'aahhhhhhhhhh whyyyyyy', 'foo', 'oook. thesse aree enoughh examplles.']
for i in s:
    print(cleanText(i))
