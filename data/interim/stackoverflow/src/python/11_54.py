def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


with open('54928944.txt', 'r') as f:
    numbers_counter = 0
    one_line_words = []
    line = f.read()
    words = line.split(' ')
    for word in words:
        if is_int(word):
            numbers_counter += 1
        else:
            numbers_counter = 0
        one_line_words.append(word)
        if numbers_counter == 3:
            print(' '.join(one_line_words))
            one_line_words = []
