def show_excitement(str,n):
        print(str)
        if(n!=1):
            show_excitement(str,n-1)

str="I am super excited for this course!"
show_excitement(str,5)
