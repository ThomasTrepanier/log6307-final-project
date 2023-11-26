def search(*args):
    arg_list = []
    search_for = numpy.append(arg_list, args)
    
    for i in strings:
        if all(j in i for j in search_for):
            print(i)
