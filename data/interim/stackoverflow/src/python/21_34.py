names = iter(['a', 'b'])

def renamer(col):
    return next(names)


df.rename(renamer, axis='columns', inplace=True)
