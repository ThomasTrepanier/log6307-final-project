def my_function(x, y):
    return f"{x}:{y}"

u = df1.assign(k=1).merge(df2.assign(k=1),on='k').drop('k',1).to_numpy()
arr = (np.array([*map(lambda x: my_function(*x),u)])
         .reshape((df1.shape[0],df2.shape[0]),order='F'))
