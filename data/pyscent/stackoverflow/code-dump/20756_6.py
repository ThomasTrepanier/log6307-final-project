def new_line(sentence: str):
    # characters that mark the end of a sentence
    end_of_sentence_markers = ['.', '!', '?', '...']
    # after n sentences insert new_line
    n = 5

    # keeps track 
    count = 0
    # final string as list for efficiency
    final_str = []
    # split at space
    sentence_split = sentence.split(' ')

    # traverse the sentence split
    for word in sentence_split:
        # if end of sentence is present then increase count
        if word[-1] in end_of_sentence_markers:
            count += 1
        # if count is equal to n then add newline otherwise add space
        if count == n:
            final_str.append(word + '\n')
            count = 0
        else:
            final_str.append(word + ' ')


    # return the string version of the list
    return ''.join(final_str)
