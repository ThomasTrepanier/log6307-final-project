def word_list(w_list, remaining_list):
    max_result_len=0
    res = w_list
    for word_index in range(len(remaining_list)):
        # if the last letter of the word list is equal to the first letter of the word
        if w_list[-1][-1] == remaining_list[word_index][0]:
            # make copies of the lists to not alter it in the caller function
            w_list_copy = w_list.copy()
            remaining_list_copy = remaining_list.copy()
            # removes the used word from the remaining list
            remaining_list_copy.pop(word_index)
            # append the matching word to the new word list
            w_list_copy.append(remaining_list[word_index])
            res_aux = word_list(w_list_copy, remaining_list_copy)
            # Keep only the longest list
            res = res_aux if len(res_aux) > max_result_len else res 
    return res

words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse']
word_list(['dog'], words)
