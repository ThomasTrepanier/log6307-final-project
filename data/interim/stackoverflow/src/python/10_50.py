def remove_dup(strng):
    '''
     Input a string and split them 
    '''
    return ', '.join(list(dict.fromkeys(strng.split(', '))))


df['Tags'] = df['Tags'].apply(lambda x: remove_dup(x))
