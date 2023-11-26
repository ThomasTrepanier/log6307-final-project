def triangle(val: str, n: int, type: str):
    for i in range(n):
        if type == "regular":
            print((i + 1) * val)
        elif type == "reversed":
            print((n - i) * val)
        elif type == "inverted":
            print((n - (i + 1)) * " " + (i + 1) * val)
        elif type == "inverted reversed":
            print(i * " " + (val * (n - i)))
        elif type == "triangle":
            print((n - (i + 1)) * " " + ((2*i)+1) * val) 
