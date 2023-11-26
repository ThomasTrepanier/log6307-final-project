def chains(words, previous_word_index=None):
    yield []
    if previous_word_index is not None:
        previous_letter = words[previous_word_index][-1]
        words = words[:previous_word_index] + words[previous_word_index + 1:]
    for i, each_word in enumerate( words ):
        if previous_word_index is None or each_word.startswith(previous_letter):
            for tail in chains(words, previous_word_index=i):
                yield [each_word] + tail  
