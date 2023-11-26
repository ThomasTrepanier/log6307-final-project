def procedures(txt1, txt2):
    str1 = txt1.lower()
    str2 = txt2.lower()
    for i in str1:
        for j in str2:
            if i == j:
                str1 = str1.replace(i, "", 1)
                str2 = str2.replace(j, "", 1)
                print("did")
    if str1 == "" and str2 == "":
        return True
    else:
        return False
