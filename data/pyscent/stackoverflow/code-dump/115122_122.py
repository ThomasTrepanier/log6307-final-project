def show_excitement(str, n):
    global return_str
    return_str += str
    if n == 0:
        return return_str
    else:
        show_excitement(str, n - 1)


return_str = ""
str = "I am super excited for this course!"
show_excitement(str, 5)
print(return_str)
