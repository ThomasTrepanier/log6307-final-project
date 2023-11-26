def show_excitement(stri,n): 
    if(n==1):
        return stri
    else:
        return show_excitement(stri,n-1)+" "+stri
print(show_excitement("I am super excited for this course!",5))
