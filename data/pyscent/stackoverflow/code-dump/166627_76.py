def get_word(my_string):
    for word in search_list:
         if word.lower() in my_string.lower():
               return word
    return None

new_df["c"]= new_df["b"].apply(get_word)
