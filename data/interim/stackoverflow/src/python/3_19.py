book_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

def printer_factory(book, n = 5):
    i = 0
    def printer():
        nonlocal i
        stop = min(i+n, len(book))
        while i < stop:
            print(book[i])
            i += 1
    return printer

printer_1 = printer_factory(book_1)

printer_1()
printer_1()
