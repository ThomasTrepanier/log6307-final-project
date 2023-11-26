def new_line_better(sentence: str, n: int):
    # final string as list for efficiency
    final_str = []
    # split at period and remove extra spaces
    sentence_split = list( map( lambda x : x.strip(),  sentence.split('.') ) )
    # pop off last space
    sentence_split.pop()
    
    # keeps track 
    count = 0
    # traverse the sentences
    for sentence in sentence_split:
        count += 1
        if count == n:
            count = 0
            final_str.append(sentence+'.\n')
        else:
            final_str.append(sentence+'. ')

    # return the string version of the list
    return ''.join(final_str)
