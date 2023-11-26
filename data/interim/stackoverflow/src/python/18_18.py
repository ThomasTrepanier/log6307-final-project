#n=Number of rows
def get_triangle(n):
    space,star=" ","* "
    for i in range(1,n+1):
         print((n-i)*space + star*i)

get_triangle(5)
