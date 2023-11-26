# this function replaces the original form of the word in the original sentence with
# the lemma form. This preserves the spacing with regard to punctuation.

def nice_lemma_sent(input_sent):
    j = 0
    lemma_sent = input_sent.text
    offset_counter = 0
    for token in input_sent:
        j += 1
        # the .idx value for the characters in the extracted sentences is based on the whole
        # document. This first if statement determines the .idx for the first token in each 
        # sentence. this is used for adjusting the offset when doing the replacement of the 
        # original word with the lemma

        if j == 1:
            first_character_position = token.idx

        # this identifies those tokens where the lemma is different. it then gets the values 
        # for the  words length and position so that slicing operations will cut them out 
        # and replace them with the lemma
        if token.text != token.lemma_:
            start_of_word = token.idx + offset_counter - first_character_position
            len_word = len(token.text)
            end_of_word = start_of_word + len_word
            len_lemma = len(token.lemma_)

            
            # substitution of the first word in the sentence if the lemma form is 
            # different from the original form
            if token.idx == first_character_position:
                residual_sent_start_position = len_word 
                lemma_sent = token.lemma_ + lemma_sent[residual_sent_start_position:]

            # substitution of subsequent words in the sentence if they are different
            # from the original form
            else:
                front_sent_end = start_of_word
                residual_sent_start = end_of_word
                lemma_sent = lemma_sent[0:front_sent_end] + token.lemma_ + \
                             lemma_sent[residual_sent_start:]

            offset_counter = len_lemma - len_word + offset_counter

    return (lemma_sent) 
