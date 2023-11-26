def replace_exception_chars(string):
    exception_chars_dict = {'Old': 'New', 'old': 'new'}

    #Iterate over key and value together
    for key, value in exception_chars_dict.items():
        #If key is found, replace key with value and assign to new string
        if key in string:
            string = string.replace(key, value)

    return string

print(replace_exception_chars('Old, not old'))
