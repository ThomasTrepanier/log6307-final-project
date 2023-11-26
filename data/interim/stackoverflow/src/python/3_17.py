book1= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
def print_book(book,a,n):
    printed = book
    if printed != []:
    
        new_list=[]#i have created a list
        for i in range(a,n+1):
            new_list.append(book[i])#append is used to add elements to list
        
        for el in new_list:
                print(el)
    
print_book(book1,0,4)#prints a,b,c,d,e
print_book(book1,5,9)#prints f,g,h,i,j
