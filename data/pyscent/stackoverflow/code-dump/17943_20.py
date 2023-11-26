def print_book(book):
    cnt = 0
    while cnt < 5:
        try:
            print(next(book))
        except StopIteration:
            print("You have reached the end!")
            break
        cnt += 1
