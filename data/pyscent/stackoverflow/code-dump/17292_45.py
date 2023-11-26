# construct an output df
output = pd.DataFrame(index=df.index, columns=df.columns)
output['Name'] = df['Name']

def findvalue(df, value):
    # check the words which contain the value
    inlist = [value in word for word in df['identifierOne']]
    try:
        # this will throw error if True is not found
        index = inlist.index(True)

        # but if there is a True, write the correct things to `output`
        one = df['identifierOne'][index]
        two = df['identifierTwo'][index]
        output.loc[df.name, 'identifierOne'] = one
        output.loc[df.name, 'identifierTwo'] = two

    except ValueError:
        return
