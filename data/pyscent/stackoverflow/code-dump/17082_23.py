a=int(input())
b=int(input())

def create_list(a,b):
    return [a**i for i in range(b+1)]

print(create_list(a,b))
