l = ['a', 'SEP', 'b', 'c', 'SEP', 'SEP', 'd']

def sublist_with_words(word, search_list):
    res = []
    for i in range(search_list.count(word)):
        index = search_list.index(word)
        res.append(search_list[:index])
        search_list = search_list[index+1:]
    res.append(search_list)
    return res
