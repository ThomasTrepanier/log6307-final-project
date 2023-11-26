_string = "Here is the content and I want to get middle words"
word_find = "content"

def get_word_indicies(input_string, word_find):
    start_index = None
    end_index = None

    for i, x in enumerate(input_string):
        if x in word_find:
            if start_index is None:
                start_index = I
            else:
                end_index = i + 1
                if (end_index - start_index) == len(word_find):
                    return [start_index, end_index]
        else:
            start_index = None
            end_index = None
    start_index = None
    end_index = None
    return [start_index,end_index]

x, y = get_word_indicies(_string, word_find)
print(_string[x:y])
