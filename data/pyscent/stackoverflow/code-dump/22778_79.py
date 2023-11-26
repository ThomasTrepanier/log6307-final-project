def myfile(filename):
    d_list = []
    with open(filename) as f:
        d_line = {}
        for line in f:
            split_line = line.rstrip("\n").split('=')  # Strip \n characters and split field and value.
            if (split_line[0] == 'name'):
                if d_line:
                    d_list.append(d_line)  # Append if there is previous line in d_line.
                d_line = {split_line[0]: split_line[1]}  # Start a new dictionary to collect the next lines.
            else:
                d_line[split_line[0]] = split_line[1]  # Add the other 2 fields to the dictionary.
        d_list.append(d_line) # Append the last line.
    return pd.DataFrame(d_list)  # Turn the list of dictionaries into a DataFrame.
