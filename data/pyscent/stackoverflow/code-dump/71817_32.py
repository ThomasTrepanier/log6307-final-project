def get_filename(path):
    temp_str = path.split('/')
    return temp_str[-1]

df["filename"] = df["filename"].apply(get_filename)
