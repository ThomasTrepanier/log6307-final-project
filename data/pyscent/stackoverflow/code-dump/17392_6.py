def dead(df):
    col_list = ['age1', 'age2']
    df = df.copy()
    temporary = df.filter(col_list)
    temporary = temporary.mask(temporary >= 100, "dead")
    df.loc[:, col_list] = temporary
    return df
