def counter(start, stop):
    x = start
    if start>stop:

        return_string = "\"Counting down: "
        while x >= stop:
            return_string += str(x)
            x=x-1
            if x>=stop:
                return_string += ","
        return_string += '"'
    else:
        return_string = "\"Counting up: "
        while x <= stop:
            return_string += str(x)
            x=x+1
            if x<=stop:
                return_string += ","
        return_string += '"'
    return return_string