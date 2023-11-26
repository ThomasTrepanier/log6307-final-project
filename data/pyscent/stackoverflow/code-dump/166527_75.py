search_list = ['STEEL','IRON','GOLD','SILVER']

def process(x):
    for s in search_list:
        if s in x['b'].upper(): print("'"+ s +"'");return "'"+ s +"'"
    return ''

df['c']= df.apply(lambda x: process(x),axis=1)
df = df.drop(df[df['c'] == ''].index).reset_index(drop=True)

print(df)
