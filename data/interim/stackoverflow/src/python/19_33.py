def valid(n):
    
    zeros = str(n).count("0")
    
    if zeros == 0:
        return False
    else:
        return zeros % 2 == 0
