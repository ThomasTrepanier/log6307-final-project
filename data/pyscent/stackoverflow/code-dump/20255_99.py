def return_int(a):
    if int(a)==a:
        print(int(a)) #you can store the integer value in separate variable #also b = int(a)
        #instead of using print you can use return b or int(a)   
    else:
        print('Error') #or you can use return 'Error'

a = 5.0
return_int(a)
