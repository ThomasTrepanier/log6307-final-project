def replaceDigits(word):
    stripped = ""
    for char in word:
        if char == "0":
            stripped += "o"
        elif not char.isdigit():
            stripped += char
    return stripped


words = ['12hell0', '123word']
stripped = [replaceDigits(n) for n in words]
print(stripped)
