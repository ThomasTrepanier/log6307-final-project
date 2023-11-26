def format_list(words, ending):
    new_list = []
    n = len(ending)
    for word in words:
        if len(word) >= n and  n > 0:
            if not word[-n:] == ending:
                new_list.append(word)
        else:
            new_list.append(word)
    return new_list 

list_words = format_list(list_words, ending)
print(list_words)
