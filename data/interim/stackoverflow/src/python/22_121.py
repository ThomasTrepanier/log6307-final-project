def show_excitement(str, n, str_built=''):
    if(n==0):
        return str_built.strip() # clear last ' '
    else:
        str_built += str + ' ' # can be changed to '\n' if needed on new line
        return show_excitement(str, n-1, str_built)


str="I am super excited for this course!"
show_excitement(str, 5) # string object
# 'I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course!'
print(show_excitement(str, 5))
# I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course!
