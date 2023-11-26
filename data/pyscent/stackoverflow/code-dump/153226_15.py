def U11():
    for i in range(1000):
        df = pd.concat([df1, df2], ignore_index=True)
        df = df.reindex(df.sort_values('c1').groupby('c1', as_index=False)['v1'].transform('min').squeeze().sort_values().index).reset_index(drop=True)

def ThePyGuy():
    for i in range(1000):
        result = []
        for i,row in df1.sort_values('v1').iterrows():
            result.append(row.to_frame().T)
            result.append(df2[df2['c1'].eq(row['c1'])].sort_values('v2'))
        df = pd.concat(result, ignore_index=True)

a = time.time()
ThePyGuy()
b = time.time()
print('ThePyGuy:', b - a)

a = time.time()
U11()
b=time.time()
print('U11:', b-a)
