def mySplit(iterable, sep):
    output = []
    sepcount = 0
    current_output = []
    for i, elem in enumerate(iterable):
        if elem != sep:
            sepcount = 0
            current_output.append(elem)
            if (i==(len(iterable)-1)):
                output.append(current_output)
        else:
            if current_output: 
                output.append(current_output)
                current_output = []

            sepcount+=1

            if (i==0) or (sepcount > 1):
                output.append([])
            if (i==(len(iterable)-1)):
                output.append([])

    return output
