def NumberStream(string):

    j=0

    for i in string:

        j=i*int(i)

        if j in string:

            return True

            break

    else:
        return False


print(NumberStream("653999923335"))
