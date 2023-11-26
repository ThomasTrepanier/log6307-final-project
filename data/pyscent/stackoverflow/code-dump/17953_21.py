book1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

def yield_book(book1):
    for i in book1:
        yield i;
                
def print_n_item(gen, n):
    count = 0
    for i in gen:
        if count == n:
            return
        print(i)
        count += 1
        
gen = yield_book(book1)
print_n_item(gen, 5) # prints a,  b,  c, d, e
print_n_item(gen, 5) # prints f,  g,  h,  i,  j
print_n_item(gen, 5) # prints k,  l,  m,  n,  o

