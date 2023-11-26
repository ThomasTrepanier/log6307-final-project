book1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

class Printer:
    def __init__(self, book):
        self.index = 0
        self.book = book

    def print(self, n):

        for i in range(0, n):
            print(self.book[self.index % len(self.book)])
            self.index += 1


book = Printer(book1)
book.print(5)
print("")
book.print(5)
print("")
book.print(7)

