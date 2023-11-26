# Python3 program to remove the @ from String


def ExceptAtTheRate(string):
    # Split the String based on the space
    arrOfStr = string.split()

    # String to store the resultant String
    res = ""

    # Traverse the words and
    # remove the first @ From every word.
    for a in arrOfStr:
        if(a[0]=='@'):
            res += a[1:len(a)] + " "
        else:
            res += a[0:len(a)] + " "

    return res


# Driver code
string = "hello @jon i am @@here or @@@there and want some@thing in '@here"

print(ExceptAtTheRate(string))
