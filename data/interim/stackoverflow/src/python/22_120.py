def show_excitement(str,n):
    if(n==0):
        print('\n') # last bit of code that runs in the function, no return
    else:
        print(str, end=' ')
        return show_excitement(str, n-1)

str="I am super excited for this course!"
show_excitement(str, 5) # returns None but prints to console

# result - note there will be space on end printed that you can't see
# I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course! I am super excited for this course!
