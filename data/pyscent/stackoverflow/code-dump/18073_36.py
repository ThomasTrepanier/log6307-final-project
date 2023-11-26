def most_frequent_letter(s):
    st = s.lower().replace(' ', '')
    frequencies = {}
    for items in st:
        if items in frequencies:
            frequencies[items] += 1
        else:
            frequencies[items] = 1
    max_val=max(frequencies.values())
    result=""
    for key,value in frequencies.items():
        if value==max_val:
            result+=key

    return result


result=most_frequent_letter('mmmaaa')
print(result)
